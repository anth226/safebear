FROM mcr.microsoft.com/devcontainers/base

# Options for setup script
ARG INSTALL_ZSH="true"
ARG UPGRADE_PACKAGES="true"
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
# Install needed packages and setup non-root user. Use a separate RUN statement to add your own dependencies.
COPY .devcontainer/library-scripts/*.sh /tmp/library-scripts/
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && /bin/bash /tmp/library-scripts/common-debian.sh "${INSTALL_ZSH}" "${USERNAME}" "${USER_UID}" "${USER_GID}" "${UPGRADE_PACKAGES}" "true" "true" \
    && apt-get install -y pkg-config zip g++ zlib1g-dev unzip python \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/library-scripts

# Install Taskfile
# https://taskfile.dev/installation/
# RUN sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d -b ~/.local/bin

# Install AWS CLI
# ARCH can either be "arm64" or "x86_64"
# ARG ARCH="x86_64"
# RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-${ARCH}.zip" -o "awscliv2.zip" && \
#     unzip awscliv2.zip && \
#     sudo ./aws/install --install-dir /usr/local/aws-cli --bin-dir /usr/local/bin &&\
#     rm -rf aws/ awscliv2.zip

# Install Poetry package manager
# RUN curl -sSL https://install.python-poetry.org | python3 - --version ${POETRY_VERSION} \
#     && rm -rf ~/.cache
# ENV PATH="~/.local/bin:$PATH"

# Install Pulumi
# https://www.pulumi.com/docs/get-started/install/
# RUN curl -fsSL https://get.pulumi.com | sh -s -- --version ${PULUMI_VERSION}
# ENV PATH "$PATH:/home/vscode/.pulumi/bin"