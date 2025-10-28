# scripts/generate_openapi.sh
#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

INPUT_URL="https://app.vouchsafe.id/openapi/swagger.json"
OUT_DIR="$REPO_ROOT/src"

# Prefer docker to avoid local Java install differences
docker run --rm -v "$REPO_ROOT":/local openapitools/openapi-generator-cli generate \
  -i "$INPUT_URL" \
  -g python \
  -o /local/src \
  --skip-validate-spec \
  --skip-overwrite \
  --global-property apis,models,modelDocs=false,apiDocs=false,apiTests=false,modelTests=false \
  --additional-properties=packageName=vouchsafe_python,projectName=vouchsafe_python