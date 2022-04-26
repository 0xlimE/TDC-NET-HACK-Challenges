# docker build -t sheller .
# docker run -p 1024:1024 --rm -it sheller
FROM ubuntu:20.04

RUN apt-get update

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY sheller .
COPY flag .
COPY ynetd .

RUN chmod +x ynetd

RUN chown -R root:root /home/ctf

USER ctf
EXPOSE 7002
CMD ./ynetd -p 7002 ./sheller