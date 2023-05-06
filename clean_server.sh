#!/usr/bin/env bash
# uninstall everything in the server

apt purge nginx nginx-common -y
rm -rf /var/www/html/*
rm -rf /data/
