FROM python:3.8-slim-buster
RUN mkdir /src
WORKDIR /src
ENV PYTHONPATH "${PYTHONPATH}:/src/"
ENV PATH "/src/scripts:${PATH}"
COPY . /src
RUN pip install -r requirements.txt
RUN chmod +x /src/scripts/*
ENTRYPOINT ["docker-entrypoint.sh"]
