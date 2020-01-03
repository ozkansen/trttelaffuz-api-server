FROM python:3.8-alpine

ENV PYTHONUNBUFFERED=1
ENV DEBUG=0
ENV CFLAGS="-O0"
ENV PORT=5000

COPY . /app
WORKDIR /app

RUN pip install -U pip --no-cache-dir
RUN apk add --update --no-cache --upgrade libxml2 libxslt
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    python3-dev gcc g++ libc-dev linux-headers libffi-dev libxml2-dev libxslt-dev \
    --repository=http://dl-cdn.alpinelinux.org/alpine/edge/main

RUN pip install -r requirements.txt --no-cache-dir

RUN apk del .tmp-build-deps

EXPOSE $PORT

CMD sh run_server.sh