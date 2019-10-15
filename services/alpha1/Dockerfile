FROM python:3.6-alpine
LABEL info="Example service 1"
WORKDIR /publish
COPY requirements.txt .
ONBUILD RUN pip3 install --upgrade pip3
RUN pip3 install -r requirements.txt
COPY . .
ARG ENV_CONFIG="config.ProductionConfig"
ENV APP_SETTINGS="${ENV_CONFIG}"
EXPOSE 5000
CMD ["python3","alpha1.py"] 