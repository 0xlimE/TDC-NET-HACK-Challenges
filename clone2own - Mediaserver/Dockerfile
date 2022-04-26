FROM ubuntu:20.04
ENV TZ=Europe/Copenhagen
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && \
    apt install mysql-server php php-mysql -y

COPY src/ /root
WORKDIR /root/LinuxMediaServerPHP
RUN chmod +x run.sh
RUN  ./run.sh
EXPOSE 80
RUN echo "TDCNET{m1d34_s5rv5r_fr4_g1thubzz}" > /tmp/$(cat /dev/urandom | tr -cd 'a-f0-9' | head -c 32)flag.txt
RUN chmod +x start.sh
CMD /root/LinuxMediaServerPHP/start.sh