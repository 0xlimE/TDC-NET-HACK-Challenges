# docker build -t sheller3 .
# docker run -p 1024:1024 --rm -it sheller3
FROM ubuntu:20.04

RUN apt-get update

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY sheller3 .
COPY flag .
COPY ynetd .

RUN chmod +x ynetd

RUN chown -R root:root /home/ctf

USER ctf
EXPOSE 7004
CMD ./ynetd -p 7004 ./sheller3