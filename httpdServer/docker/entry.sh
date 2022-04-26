#!/bin/bash

while true
do
    ./httpd &
    echo $! > /tmp/pid
    sleep 15
    pkill -TERM -P `cat /tmp/pid`
    kill `cat /tmp/pid`
done