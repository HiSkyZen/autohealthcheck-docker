FROM ubuntu:20.04

LABEL maintainer="mchan030704@gmail.com"

RUN ln -s /usr/bin/* /usr/sbin/ -f

RUN mkdir moemoekyun
WORKDIR /moemoekyun
COPY ./main.py /moemoekyun/main.py
#COPY . .
#RUN chmod -R 774 *

RUN apt update
RUN apt upgrade -y

RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y tzdata locales

RUN locale-gen ko_KR.UTF-8
ENV LC_ALL=ko_KR.UTF-8
ENV TZ=Asia/Seoul

RUN apt install python3-pip -y

RUN pip3 install hcskr

ENV NAME=홍길동
ENV BIRTH=010101
ENV REGION=OO시교육청
ENV SCHOOL=OO고등학교
ENV SCHOOL_LEVEL=고등학교
ENV PASSWORD=0000

ENTRYPOINT ["python3", "./main.py"]