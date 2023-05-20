#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static

# install nginx only if it is not installed in it
if ! command -v nginx &> /dev/null
then
    apt-get update
    apt-get install nginx -y
fi

# creates the index page and error page
echo "Hello World!" > /var/www/html/index.html
echo "Ceci n'est pas une page" > /var/www/html/not_found.html

# creates data directory and all of it sub directories
mkdir -p /data/web_static/releases/test/ 
mkdir -p /data/web_static/shared/

echo "Hello Holberton" > /data/web_static/releases/test/index.html

# symbolic link to the test directory
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -h -R ubuntu:ubuntu /data/

nginx_conf="server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
	# Add index.php to the list if you are using PHP
	index index.html index.htm index.nginx-debian.html;

	server_name _;
	add_header X-Served-By $HOSTNAME;

	location / {
		try_files \$uri \$uri/ =404;
	}
	location /redirect_me {
			return 301 https://jojoport.netlify.app;
	}
	location /hbnb_static {
		alias /data/web_static/current;
		index index.html index.htm;
	}
	error_page 404 /not_found.html;
	location = /not_found.html{
		internal;
	}
}"

echo -e "$nginx_conf" > /etc/nginx/sites-available/default

service nginx restart
