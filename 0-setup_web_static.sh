#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static

# install nginx only if it is not installed in it
if ! command -v nginx > /dev/null
then
    apt-get update -y
    apt-get install nginx -y
    service nginx start
fi

redirect="\tlocation /redirect_me {\n\t\treturn 301 https://jojoport.netlify.com;\n\t}"
error="\terror_page 404 /not_found.html;"   
echo  "Hello World!" > /var/www/html/index.html
echo "Ceci n'est pas une page" > /var/www/html/not_found.html
sed -i "/server_name _;/a\ \n${redirect}\n" /etc/nginx/sites-available/default
sed -i "/server_name _;/a\ \n${error}\n" /etc/nginx/sites-available/default
sed -i "/server_name _;/a\ \tadd_header X-Served-By \$HOSTNAME always;" /etc/nginx/sites-available/default                                                            
 

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
sed -i "/server_name _;/a\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\tindex index.html index.htm;\n\t}" /etc/nginx/sites-available/default
service nginx restart
