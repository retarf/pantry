FROM python:3.10.4

ARG DB_HOST
ARG DB_PORT

COPY backend backend
COPY config/scripts /scripts
WORKDIR /backend
RUN pip install -r requirements.txt
RUN ["chmod","+x","/scripts/connection_test"]
RUN ["chmod","+x","/scripts/run.sh"]

CMD ["sh","-c","/scripts/run.sh"]
