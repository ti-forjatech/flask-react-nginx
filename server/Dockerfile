FROM python:3.7-slim

ENV CONTAINER_HOME=/var/www
WORKDIR $CONTAINER_HOME


# keep the parent server directory structure for relative imports
RUN mkdir server
ADD server $CONTAINER_HOME/server

CMD ["python3", "-m", "venv", "venv"]

RUN pip install --no-cache-dir -r server/requirements.txt