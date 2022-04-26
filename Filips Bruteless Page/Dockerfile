FROM ubuntu:18.04
WORKDIR /var/www/html
RUN apt-get update
ENV TZ=Europe/Copenhagen
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get install -qq -y php  
WORKDIR /var/www
COPY src/ webapp/
RUN echo "TDCNET{n0p455w02dc24ck1n9w4523qu123d!!}" > /tmp/$(cat /dev/urandom | tr -cd 'a-f0-9' | head -c 32)flag.txt
EXPOSE 80
CMD ["/bin/bash","/var/www/webapp/start.sh"]