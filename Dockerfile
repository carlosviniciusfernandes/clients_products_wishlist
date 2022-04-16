FROM ubuntu:latest

WORKDIR /app/

RUN apt update && apt upgrade -y
RUN apt install -y -q python3-pip python3-dev
RUN pip3 install -U pip setuptools wheel
RUN apt install python3.8-venv

EXPOSE 8000
EXPOSE 5678
