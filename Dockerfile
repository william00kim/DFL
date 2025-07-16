FROM nvidia/cuda:12.8.1-cudnn-devel-ubuntu22.04

RUN apt update && \
apt install -y wget

RUN mkdir -p ~/miniconda3 && \
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh && \
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3 && \
rm ~/miniconda3/miniconda.sh

WORKDIR /work
COPY . /work

RUN . ~/miniconda3/bin/activate && \
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main && \
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r && \
conda init && \
conda env create -f LLMfile/langchain_env.yml -n Langchain