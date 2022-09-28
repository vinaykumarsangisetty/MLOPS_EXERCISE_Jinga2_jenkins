FROM ubuntu:latest
WORKDIR /usr/app/
COPY . /usr/app/
EXPOSE 7000
RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get update && apt-get -y install libpq-dev gcc && pip install psycopg2
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD uvicorn app:app --host 0.0.0.0 --port 7000 --reload