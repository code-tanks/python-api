FROM ubuntu:focal

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y sudo && \
    apt-get install -y software-properties-common --no-install-recommends && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y wget curl git python3.9 python3-distutils gpg-agent --no-install-recommends && \
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3 get-pip.py && \
    pip install pylint autopep8

RUN useradd -ms /bin/bash developer
USER developer
WORKDIR /home/developer
