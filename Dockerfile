FROM python:3.12-alpine
RUN apk add --update python3 py3-pip
RUN pip install xmlrunner

WORKDIR /app

COPY . . 

CMD ["python3", "tests.py"]
