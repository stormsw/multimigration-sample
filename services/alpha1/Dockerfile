FROM python:3.6-alpine
LABEL info="Example service Alpha1"
ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING=UTF-8

RUN pip3 install --upgrade pip

WORKDIR /publish
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .

ENV LISTEN_PORT=5000
ENV DEBUG_PORT=3000
# You can override the config to one of the: ProductionConfig,StagingConfig,DevelopmentConfig,TestingConfig
ARG CONF="config.ProductionConfig"

ENV APP_SETTINGS="${CONF}"
ENV FLASK_APP="alpha1.py"
# This allows to start debugging in the docker
ENTRYPOINT [ "/bin/sh","-c","python3 -m ptvsd --host 0.0.0.0 --port ${DEBUG_PORT} -m flask run --no-debugger --no-reload --port=${LISTEN_PORT} --host=0.0.0.0" ]

EXPOSE ${LISTEN_PORT}
EXPOSE ${DEBUG_PORT}
