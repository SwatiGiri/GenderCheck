from ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

WORKDIR /app

COPY . /app

RUN pip3 install -r Other_requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["main.py"]
