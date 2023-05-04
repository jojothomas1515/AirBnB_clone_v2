#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static

# install nginx only if it is not installed in it
if ! command -v nginx > /dev/null
then
    apt-get update -y
    apt-get install nginx -y
    service nginx start
fi

# data to test nnginx with
fakeData="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

# the p flag make it so that it create the the parent directories in the path if it doesn't exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo -e "$fakeData" > /data/web_static/releases/test/index.html

ln -s /data/web_static/releases/test/ /data/web_static/current -f

chown -R ubuntu:ubuntu /data/

sed -i "/server_name _;/a\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default

sed -i "/server_name _;/a\ \tadd_header X-Served-By \$HOSTNAME always;" /etc/nginx/sites-available/default

service nginx restart
