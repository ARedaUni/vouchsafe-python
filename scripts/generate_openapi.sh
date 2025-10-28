#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

INPUT_URL="https://app.vouchsafe.id/openapi/swagger.json"
OUT_DIR="$REPO_ROOT/src"

# Generate to a temp directory first
TEMP_DIR=$(mktemp -d)

docker run --rm -v "$TEMP_DIR":/local openapitools/openapi-generator-cli generate \
  -i "$INPUT_URL" \
  -g python \
  -o /local \
  --skip-validate-spec \
  --additional-properties=packageName=vouchsafe_python,projectName=vouchsafe_python,generateSupportingFiles=true,apiTests=false,modelTests=false,modelDocs=false,apiDocs=false

# Create output directory
mkdir -p "$OUT_DIR/vouchsafe_python"

# Copy only the files you need
cp -r "$TEMP_DIR/vouchsafe_python/api" "$OUT_DIR/vouchsafe_python/"
cp -r "$TEMP_DIR/vouchsafe_python/models" "$OUT_DIR/vouchsafe_python/"
cp "$TEMP_DIR/vouchsafe_python/__init__.py" "$OUT_DIR/vouchsafe_python/"
cp "$TEMP_DIR/vouchsafe_python/configuration.py" "$OUT_DIR/vouchsafe_python/"
cp "$TEMP_DIR/vouchsafe_python/exceptions.py" "$OUT_DIR/vouchsafe_python/"
cp "$TEMP_DIR/vouchsafe_python/rest.py" "$OUT_DIR/vouchsafe_python/"
cp "$TEMP_DIR/vouchsafe_python/api_client.py" "$OUT_DIR/vouchsafe_python/"
cp "$TEMP_DIR/vouchsafe_python/api_response.py" "$OUT_DIR/vouchsafe_python/"

# Optional: copy py.typed if you want type checking support
[ -f "$TEMP_DIR/vouchsafe_python/py.typed" ] && cp "$TEMP_DIR/vouchsafe_python/py.typed" "$OUT_DIR/vouchsafe_python/"

# Clean up temp directory
rm -rf "$TEMP_DIR"

echo "✓ Generated SDK files to $OUT_DIR/vouchsafe_python"