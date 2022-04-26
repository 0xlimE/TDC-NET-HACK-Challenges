#!/bin/bash
rm /root/start.sh
cd /var/www/ghosts && php -S 127.0.0.1:8001 &
cd /var/www/spookyadminservice && php -S 127.0.0.1:8000 &
service nginx start
tail -f /dev/null