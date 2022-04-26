# docker build -t sheller2 .
# docker run -p 1024:1024 --rm -it sheller2
FROM ubuntu:20.04

RUN apt-get update

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY sheller2 .
COPY flag .
COPY ynetd .

RUN chmod +x ynetd

RUN chown -R root:root /home/ctf

USER ctf
EXPOSE 7003
CMD ./ynetd -p 7003 ./sheller2