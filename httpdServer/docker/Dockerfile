# docker build -t xiewenzhou .
# docker run -p 1024:1024 --rm -it xiewenzhou
FROM ubuntu:20.04

RUN apt-get update

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /
COPY flag ./flag6470e394cbf6dab6a91682cc8585059b

WORKDIR /home/ctf
RUN mkdir htdocs
COPY httpd .
COPY entry.sh .


RUN chmod +x entry.sh

RUN chown -R root:root /home/ctf

USER ctf
EXPOSE 8080
CMD ./entry.sh