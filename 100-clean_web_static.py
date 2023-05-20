#!/usr/bin/python3
"""Distribute the compressed version of  web_static\
folder of your AirBnB Clone repo."""
from fabric.api import env, run, put, local

env.hosts = ['34.205.65.154', '34.239.107.150']
env.user = 'ubuntu'


def do_clean(number=0):
    """Cleanup."""

    try:
        data = run("ls -tr /data/web_static/releases| head -n -{}"\
                   "|xargs rm -rf".format(number))
    except Exception:
        pass