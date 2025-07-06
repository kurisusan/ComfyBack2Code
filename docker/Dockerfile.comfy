ARG CUDA_VERSION=12.9.1
ARG UBUNTU_VERSION=24.04
FROM nvidia/cuda:${CUDA_VERSION}-cudnn-devel-ubuntu${UBUNTU_VERSION}
ENV DEBIAN_FRONTEND=noninteractive

ENV TORCH_CUDA_ARCH_LIST="8.9"
# ENV PIP_BREAK_SYSTEM_PACKAGES=1


RUN apt-get update && apt-get install -y --no-install-recommends \
    # Ajout du PPA pour Python 3.11
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    # Installation des paquets
    && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    python3.11 \
    python3.11-venv \
    python3.11-dev \
    libgl1 \
    wget \
    curl \
    nano \
    ffmpeg \
    zsh \
    libglib2.0-0 \
    # Nettoyage final
    && rm -rf /var/lib/apt/lists/*

# Configurer le répertoire de travail
WORKDIR /app

RUN git clone https://github.com/comfyanonymous/ComfyUI .

ENV VPIP=/app/venv/bin/pip
RUN python3.11 -m venv venv
RUN $VPIP install --pre torch torchvision torchaudio triton --index-url https://download.pytorch.org/whl/nightly/cu128
RUN $VPIP install onnxruntime-gpu imageio-ffmpeg
RUN $VPIP install -r requirements.txt
RUN $VPIP install -U sageattention

COPY ./extra_model_paths.yaml /app/extra_model_paths.yaml

# ==============================================================================
# INSTALLATION DES CUSTOM NODES
# ==============================================================================
WORKDIR /app/custom_nodes

ENV NODE_LIST_FILE="/tmp/custom-nodes.txt"
COPY custom-nodes.txt $NODE_LIST_FILE
COPY custom-nodes-loader.sh /usr/local/bin/custom-nodes-loader.sh

# Donnez les droits d'exécution au script et lancez-le
RUN chmod +x /usr/local/bin/custom-nodes-loader.sh && \
    custom-nodes-loader.sh

WORKDIR /app


# Exposer le port
EXPOSE 8188


RUN usermod -s /usr/bin/zsh root
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

SHELL ["/bin/zsh", "-c"]

# Commande de lancement avec le venv activé
CMD [ \
    "./venv/bin/python", \
    "main.py", \
    # "--gpu-only", \
    "--listen", \
    "0.0.0.0" \
    ]
