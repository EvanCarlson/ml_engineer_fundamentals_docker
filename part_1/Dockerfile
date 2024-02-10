FROM python:alpine3.19

LABEL maintainer="youremail@address.com"

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]