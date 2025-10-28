import asyncio
from datetime import datetime, timedelta
from typing import Optional, Union

from openapi import (
    AuthenticationApi,
    VerificationsApi,
    SmartLookupsApi,
    FlowsApi,
    AuthenticateInput,
    Configuration,
    ApiClient,
    ApiException
)
from openapi.models import (
    RequestVerificationInput,
    SmartLookupInput,
    Status
)


class VouchsafeApiError(Exception):
    """Custom exception for Vouchsafe API errors"""
    
    def __init__(self, status_code: int, response_body: dict, message: Optional[str] = None):
        self.status_code = status_code
        self.response_body = response_body
        super().__init__(message or str(response_body))


class VouchsafeClient:
    """A high-level client for interacting with the Vouchsafe API.
    
    This client handles authentication token management, error handling,
    and provides convenient methods for common operations.
    """
    
    def __init__(self, client_id: str, client_secret: str, base_url: str = "https://app.vouchsafe.id/api/v1"):
        """
        Initialize the Vouchsafe client.
        
        Args:
            client_id: Your Vouchsafe client ID
            client_secret: Your Vouchsafe client secret
            base_url: The base URL for the Vouchsafe API (defaults to production)
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = base_url
        
        # Token management
        self.token: Optional[str] = None
        self.token_expiry: Optional[datetime] = None
        
        # Initialize configuration and API instances
        self.config = Configuration(host=base_url)
        self.api_client = ApiClient(self.config)
        
        # Initialize API instances
        self.authentication_api = AuthenticationApi(self.api_client)
        self.verifications_api = VerificationsApi(self.api_client)
        self.smart_lookups_api = SmartLookupsApi(self.api_client) 
        self.flows_api = FlowsApi(self.api_client)
    
    def _should_refresh_token(self) -> bool:
        """Check if the current token should be refreshed."""
        if not self.token or not self.token_expiry:
            return True
        
        # Refresh if within 5 minutes of expiry
        buffer_time = timedelta(minutes=5)
        return datetime.now() >= (self.token_expiry - buffer_time)
    
    async def _get_access_token(self) -> str:
        """Get a valid access token, refreshing if needed."""
        if self._should_refresh_token():
            try:
                auth_input = AuthenticateInput(
                    client_id=self.client_id,
                    client_secret=self.client_secret
                )
                
                response = self.authentication_api.authenticate(authenticate_input=auth_input)
                
                self.token = response.access_token
                self.token_expiry = datetime.fromisoformat(response.expires_at.replace('Z', '+00:00'))
                
                self.config.access_token = self.token
            except ApiException as e:
                raise VouchsafeApiError(
                    status_code=e.status,
                    response_body=e.body,
                    message=f"Failed to authenticate: {e.reason}"
                )
        
        return self.token
    
    async def _with_error_handling(self, api_call):
        """Wrapper to handle API errors and re-authenticate on 401."""
        try:
            return api_call()
        except ApiException as e:
            if e.status == 401:
                # Force a token refresh and retry once
                self.token = None
                self.token_expiry = None
                await self._get_access_token()
                
                # Retry the original call
                return api_call()
            elif e.body:
                try:
                    import json
                    body = json.loads(e.body)
                    message = body.get('message', e.reason)
                except (json.JSONDecodeError, TypeError):
                    body = {}
                    message = e.reason
                raise VouchsafeApiError(
                    status_code=e.status,
                    response_body=body,
                    message=message
                )
            else:
                raise VouchsafeApiError(
                    status_code=e.status,
                    response_body={},
                    message=e.reason
                )
    
    # Public methods for verifications
    
    async def get_verification(self, verification_id: str):
        """Get a single verification by ID."""
        await self._get_access_token()
        
        def api_call():
            return self.verifications_api.get_verification(id=verification_id)
        
        return await self._with_error_handling(api_call)
    
    async def list_verifications(self, status: Optional[Status] = None):
        """List all verifications for your team."""
        await self._get_access_token()
        
        def api_call():
            return self.verifications_api.list_verifications(status=status)
        
        return await self._with_error_handling(api_call)
    
    async def request_verification(self, input_data: RequestVerificationInput):
        """Request a new verification."""
        await self._get_access_token()
        
        def api_call():
            return self.verifications_api.request_verification(request_verification_input=input_data)
        
        return await self._with_error_handling(api_call)
    
    # Public methods for smart lookups
    
    async def perform_smart_lookup(self, input_data: SmartLookupInput):
        """Perform a smart lookup."""
        await self._get_access_token()
        
        def api_call():
            return self.smart_lookups_api.perform_smart_lookup(smart_lookup_input=input_data)
        
        return await self._with_error_handling(api_call)
    
    async def search_postcode(self, postcode: str):
        """Search for addresses by postcode."""
        await self._get_access_token()
        
        def api_call():
            return self.smart_lookups_api.search_postcode(postcode=postcode)
        
        return await self._with_error_handling(api_call)
    
    # Public methods for flows
    
    async def list_flows(self):
        """Get a list of all currently published verification flows."""
        await self._get_access_token()
        
        def api_call():
            return self.flows_api.list_flows()
        
        return await self._with_error_handling(api_call)
    
    async def get_flow(self, flow_id: str):
        """Get a specific verification flow."""
        await self._get_access_token()
        
        def api_call():
            return self.flows_api.get_flow(id=flow_id)
        
        return await self._with_error_handling(api_call)