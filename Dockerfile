FROM python:3.8-slim-buster
WORKDIR /src
ENV PYTHONPATH "${PYTHONPATH}:/src/"
ENV PATH "/src/scripts:${PATH}"
COPY . /src
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
RUN chmod +x /src/scripts/*
ENTRYPOINT ["docker-entrypoint.sh"]
