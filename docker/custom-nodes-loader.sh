#!/bin/bash
set -e

# --- Configuration ---
TARGET_DIR="/app/custom_nodes" 
# TARGET_DIR="test" 

# --- Exécution ---
echo "Moving to target directory: ${TARGET_DIR}"
cd "${TARGET_DIR}"

echo "--- Starting Node Cloning Process from ${NODE_LIST_FILE} ---"
mapfile -t urls < <(grep -v '^\s*#' "${NODE_LIST_FILE}" | grep -v '^\s*$' | tr -d '\r')
for url in "${urls[@]}"; do
    echo "Cloning ${url}"
    if ! git clone "${url}"; then
        echo "WARNING: Failed to clone ${url}"
    fi
done

echo "--- Cloning complete. Installing Python dependencies. ---"
for dir in */; do
    if [[ -f "${dir}requirements.txt" ]]; then
        echo "Installing requirements for ${dir}"
        ${VPIP:-pip} install --no-cache-dir -r "${dir}requirements.txt"
    fi
done

echo "--- Installing special requirements (nunchaku wheel) ---"
${VPIP:-pip} install https://huggingface.co/mit-han-lab/nunchaku/resolve/main/nunchaku-0.3.1+torch2.8-cp311-cp311-linux_x86_64.whl

echo "--- Node installation process finished successfully. ---"

rm "${NODE_LIST_FILE}"