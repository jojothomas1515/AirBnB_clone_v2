#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static

# install nginx only if it is not installed in it
if ! command -V nginx &> /dev/null
then
    apt-get update -y
    apt-get install nginx -y
fi

# creates the index page and error page
echo "Hello World!" > /var/www/html/index.html
echo "Ceci n'est pas une page" > /var/www/html/not_found.html

# creates data directory and all of it sub directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared

echo "Hello Holberton" > /data/web_static/releases/test/index.html

# symbolic link to the test directory
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

nginx_conf="
server {
       listen 80 default_server;
       listen [::]:80 default_server;

       root /var/www/html;

       server_name _;

       add_header X-Served-By \$HOSTNAME always;

       error_page 404 /not_found.html;

       location / {
       		try_files \$uri \$uri/ =404;
	}

	location /redirect_me {
		 return 301 https://jojoport.netlify.com;
	}

	location /hbnb_static {
		 alias /data/web_static/current/;
		 try_files \$uri \$uri/ =404;
	}
}
"

echo -e "$nginx_conf" > /etc/nginx/sites-available/web_static
ln -sf /etc/nginx/sites-available/web_static /etc/nginx/sites-enabled/web_static
rm -f /etc/nginx/sites-enabled/default

service nginx restart
