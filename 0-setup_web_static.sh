#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static

# Updating packages for installation
sudo apt-get update && sudo apt-get upgrade

# Installing nginx server
sudo apt-get install nginx -y

# Creating folders for the deployment
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Creating fake html file
sudo echo "<html>
     <head><title>  </title>
     </head>
     <body>
	fake html file
     </body>
     </html>" | sudo tee /data/web_static/releases/test/index.html

# Creating symbolic link between directories
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Giving ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Updating nginx configuration
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Testing configurations
sudo nginx -t

# restarting nginx server
sudo service nginx restart
