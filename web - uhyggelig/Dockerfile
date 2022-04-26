FROM ubuntu:18.04
WORKDIR /var/www/html
RUN apt-get update
ENV TZ=Europe/Copenhagen
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get install -qq -y php nginx 
WORKDIR /var/www
COPY src/ ghosts/
COPY src2/ spookyadminservice/
COPY default.conf /etc/nginx/sites-enabled/default
COPY start.sh /root/start.sh
RUN echo "TDCNET{uhygg3l1g_sp0g3ls3_fr4_TDC_n3T_p3nt35t}" > /tmp/$(cat /dev/urandom | tr -cd 'a-f0-9' | head -c 32)flag.txt
EXPOSE 25999
CMD ["/bin/bash","/root/start.sh"]