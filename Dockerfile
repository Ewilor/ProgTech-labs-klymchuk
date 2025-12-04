FROM python:3.9-alpine
RUN apk add --no-cache build-base
RUN pip3 install xmlrunner

WORKDIR /app

COPY . . 

CMD ["python3", "tests.py"]
