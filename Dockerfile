FROM python:3.8-alpine
WORKDIR /app
RUN apk add --no-cache --virtual .build-deps gcc musl-dev
COPY ./registration /app
RUN pip3 install -r requirements.txt
RUN apk del .build-deps gcc musl-dev
CMD python3 main.py