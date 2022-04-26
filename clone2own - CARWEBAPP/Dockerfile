FROM ubuntu:20.04
ENV TZ=Europe/Copenhagen
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && \
    apt install python3-pip openjdk-8-jdk -y

COPY src/ /root/CARWEBAPP
WORKDIR /root/CARWEBAPP
RUN pip3 install -r requirements.txt
RUN echo "TDCNET{t3ll_u5_h0w_U_s0lv3d_th15_h3h3}" > /tmp/$(cat /dev/urandom | tr -cd 'a-f0-9' | head -c 32)flag.txt
EXPOSE 80
CMD ["python3","/root/CARWEBAPP/app.py"]