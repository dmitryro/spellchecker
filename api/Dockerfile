FROM python:3.8.5-alpine
ENV C_FORCE_ROOT true

ENV PIP_FORMAT=legacy
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV DEBUG true

COPY . /api
WORKDIR /api

COPY . .
RUN chmod +x ./run.sh

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add --no-cache bash libxml2-dev libxslt-dev gcc python3-dev linux-headers musl-dev openssl-dev libffi-dev build-base

RUN pip install --upgrade pip
# install requirements
RUN pip install -r requirements.txt
# Run gunicorn
CMD ["./run.sh"]
