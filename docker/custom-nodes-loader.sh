#!/bin/bash
# Script pour cloner les nodes custom de ComfyUI et installer leurs dépendances.

# 'set -e' fait en sorte que le script s'arrête immédiatement si une commande échoue.
set -e

# --- Configuration ---
# Assurez-vous que ce chemin correspond bien à votre dossier de custom nodes
TARGET_DIR="/app/custom_nodes" 

# --- Exécution ---
echo "Moving to target directory: ${TARGET_DIR}"
cd "${TARGET_DIR}"

echo "--- Starting Node Cloning Process from ${NODE_LIST_FILE} ---"
while IFS= read -r url; do
    echo "Cloning ${url}"
    git clone "${url}"
done < "${NODE_LIST_FILE}"

echo "--- Cloning complete. Installing Python dependencies. ---"
for dir in */; do
    if [ -f "${dir}requirements.txt" ]; then
        echo "Installing requirements for ${dir}"
        # Utilise la variable $VPIP de votre Dockerfile, avec 'pip' comme solution de repli
        ${VPIP:-pip} install --no-cache-dir -r "${dir}requirements.txt"
    fi
done

echo "--- Installing special requirements (nunchaku wheel) ---"
${VPIP:-pip} install https://huggingface.co/mit-han-lab/nunchaku/resolve/main/nunchaku-0.3.1+torch2.8-cp311-cp311-linux_x86_64.whl

echo "--- Node installation process finished successfully. ---"

# On peut aussi supprimer le fichier de liste à la fin
rm "${NODE_LIST_FILE}"