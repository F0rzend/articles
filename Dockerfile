FROM python:3.8-slim-buster
RUN apt-get update; apt-get install -y curl && mkdir /src
WORKDIR /src
ENV PYTHONPATH "${PYTHONPATH}:/src/"
ENV PATH "/src/scripts:${PATH}"
COPY . /src
RUN pip install -r requirements.txt
RUN chmod +x /src/scripts/*
ENTRYPOINT ["docker-entrypoint.sh"]
