# docker build -t cursed .
# docker run -p 1024:1024 --rm -it cursed
FROM ubuntu:20.04

RUN dpkg --add-architecture i386
RUN apt-get update -y
RUN apt-get install -y libc6-dbg libc6-dbg:i386 lib32stdc++6 

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf

RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY cursed .
COPY flag .
COPY ynetd .

RUN chmod +x ynetd

RUN chown -R root:root /home/ctf

USER ctf
EXPOSE 1024
CMD ./ynetd -p 1024 ./cursed