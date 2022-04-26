service mysql start
echo quit | mysql
mysql < root.sql
service mysql restart
mysql -u newuser -ppassword < createcinema.sql
mysql -u newuser -ppassword -D cinema < cinema.sql

