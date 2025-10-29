from datetime import datetime, timedelta
from typing import Optional

from .api import (
    AuthenticationApi,
    VerificationsApi,
    SmartLookupsApi,
    FlowsApi
)
from .api_client import ApiClient
from .configuration import Configuration
from .exceptions import ApiException
from .models import (
    RequestVerificationInput,
    SmartLookupInput,
    Status,
    AuthenticateInput
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
    
    def _get_access_token(self) -> str:
        """Get a valid access token, refreshing if needed."""
        # Check if token is still valid (with 5-minute buffer)
        if self.token and self.token_expiry:
            buffer_time = timedelta(minutes=5)
            if datetime.now() < (self.token_expiry - buffer_time):
                return self.token
        
        # Need to refresh token
        try:
            auth_input = AuthenticateInput(
                client_id=self.client_id,
                client_secret=self.client_secret
            )
            
            response = self.authentication_api.authenticate(authenticate_input=auth_input)
            
            self.token = response.access_token
            self.token_expiry = datetime.fromisoformat(response.expires_at.replace('Z', '+00:00'))
            
            # Set token in API client's default headers
            self.api_client.default_headers['Authorization'] = f'Bearer {self.token}'
            
        except ApiException as e:
            raise VouchsafeApiError(
                status_code=e.status,
                response_body=e.body if e.body else {},
                message=f"Failed to authenticate: {e.reason}"
            )
        
        return self.token
    
    def _with_error_handling(self, api_call):
        """Wrapper to handle API errors and re-authenticate on 401."""
        try:
            return api_call()
        except ApiException as e:
            if e.status == 401:
                # Force a token refresh and retry once
                self.token = None
                self.token_expiry = None
                self._get_access_token()
                
                # Retry the original call
                return api_call()
            
            # Handle other errors
            if e.body:
                try:
                    import json
                    body = json.loads(e.body) if isinstance(e.body, str) else e.body
                    message = body.get('message', e.reason)
                except (json.JSONDecodeError, TypeError):
                    body = {}
                    message = e.reason
            else:
                body = {}
                message = e.reason
                
            raise VouchsafeApiError(
                status_code=e.status,
                response_body=body,
                message=message
            )
    
    # Public methods for verifications
    
    def get_verification(self, verification_id: str):
        """Get a single verification by ID."""
        self._get_access_token()
        
        return self._with_error_handling(
            lambda: self.verifications_api.get_verification(id=verification_id)
        )
    
    def list_verifications(self, status: Optional[Status] = None):
        """List all verifications for your team."""
        self._get_access_token()
        
        return self._with_error_handling(
            lambda: self.verifications_api.list_verifications(status=status)
        )
    
    def request_verification(self, input_data: RequestVerificationInput):
        """Request a new verification."""
        self._get_access_token()
        
        return self._with_error_handling(
            lambda: self.verifications_api.request_verification(request_verification_input=input_data)
        )
    
    # Public methods for smart lookups
    
    def perform_smart_lookup(self, input_data: SmartLookupInput):
        """Perform a smart lookup."""
        self._get_access_token()
        
        return self._with_error_handling(
            lambda: self.smart_lookups_api.perform_smart_lookup(smart_lookup_input=input_data)
        )
    
    def search_postcode(self, postcode: str):
        """Search for addresses by postcode."""
        self._get_access_token()
        
        return self._with_error_handling(
            lambda: self.smart_lookups_api.search_postcode(postcode=postcode)
        )
    
    # Public methods for flows
    
    def list_flows(self):
        """Get a list of all currently published verification flows."""
        self._get_access_token()
        
        return self._with_error_handling(
            lambda: self.flows_api.list_flows()
        )
    
    def get_flow(self, flow_id: str):
        """Get a specific verification flow."""
        self._get_access_token()
        
        return self._with_error_handling(
            lambda: self.flows_api.get_flow(id=flow_id)
        )