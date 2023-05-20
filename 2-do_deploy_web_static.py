#!/usr/bin/python3
"""Distribute the compressed version of  web_static\
folder of your AirBnB Clone repo."""
from fabric.api import env, run, put
import time
import pathlib as pl
import os

env.hosts = ['34.205.65.154', '34.239.107.150']
env.user = 'ubuntu'


def do_deploy(archive_path: str) -> str or None:
    """Push a specified archive in my server.

    arguments:
        archive_path: the path of the archive to be sent.
    """
    if not pl.Path(archive_path).is_file():
        return False

    filenamew = archive_path.split(".")[0].split("/")[-1]
    try:
        ans = put(archive_path, "/tmp/")
        run ("mkdir -p /data/web_static/releases/{}".format(filenamew))
        run ("tar -xf {} -C /data/web_static/releases/{}".format(ans[0],
                                                                 filenamew))
        run ("mv -r /data/web_static/releases/{name}/web_static/*" \
             "/data/web_static/releases/{name}/"
             .format(name=filenamew))
        run("rm {}".format(ans[0]))
        run("rm /data/web_static/releases/{}/web_static".format(filenamew))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current"
            .format(filenamew)
        return True
    except Exception:
        return False
