ARG PYTHON_VERSION="3.11"
ARG POETRY_VERSION="1.4.2"

FROM amazonlinux:2023 AS base
# Install Python
ARG PYTHON_VERSION
RUN yum -y install \
    which \
    python${PYTHON_VERSION} \
    python${PYTHON_VERSION}-pip \
    python${PYTHON_VERSION}-wheel \
    && yum -y clean all \
    && rm -rf /var/cache/yum \
    && pip${PYTHON_VERSION} install --no-cache-dir --upgrade pip
# Set the Lambda root directory
ENV LAMBDA_TASK_ROOT=/var/task
RUN mkdir -p ${LAMBDA_TASK_ROOT}
WORKDIR ${LAMBDA_TASK_ROOT}
# Install Poetry package manager
# https://python-poetry.org/docs/
ARG POETRY_VERSION
ENV POETRY_VERSION=${POETRY_VERSION}
ENV POETRY_HOME="/opt/poetry"
RUN curl -sSL https://install.python-poetry.org/ | python${PYTHON_VERSION} && rm -rf ~/.cache
ENV PATH="${POETRY_HOME}/bin:${PATH}"
# Create a virtual environment
ENV VIRTUAL_ENV="/opt/venv"
RUN python${PYTHON_VERSION} -m venv ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"
# Install AWS Lambda Runtime Interface Client
RUN pip install --no-cache-dir awslambdaric
ENTRYPOINT [ "python", "-m", "awslambdaric" ]

FROM base AS graphql
ARG PROJECT=projects/api
WORKDIR ${LAMBDA_TASK_ROOT}/${PROJECT}
# Install dependencies
COPY ${PROJECT}/poetry.lock ${PROJECT}/pyproject.toml ./
ADD libs/shared ${LAMBDA_TASK_ROOT}/libs/shared
RUN --mount=type=cache,mode=0777,target=/home/.cache/pypoetry \
    poetry install --only main
# Copy the source code
ADD ${PROJECT}/src ./src

FROM graphql AS admin
CMD [ "src.lambda_function.admin_handler" ]

FROM graphql AS app
CMD [ "src.lambda_function.app_handler" ]