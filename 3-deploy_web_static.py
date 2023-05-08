#!/usr/bin/python3
"""Distribute the compressed version of  web_static\
folder of your AirBnB Clone repo."""
from fabric.api import env, run, put, local
import time
import pathlib as pl
import os

env.hosts = ['34.205.65.154', '34.239.107.150']
env.user = 'ubuntu'


def do_pack():
    """Compresses web static and add it to versions."""
    if not pl.Path("versions").is_dir():
        os.makedirs("versions")
    mypath = "versions/web_static_{}.tgz".format(
        time.strftime("%Y%m%d%H%M%S"))
    res = local("tar caf {paths} web_static/"
                .format(paths=mypath), )

    if not pl.Path(mypath).is_file():
        return None
    return pl.Path(mypath).absolute()


def do_deploy(archive_path: str) -> str or None:
    """Push a specified archive in my server.

    arguments:
        archive_path: the path of the archive to be sent.
    """
    try:
        a_path = pl.Path(archive_path).absolute()
        name = pl.Path(a_path).name
        dest = "/data/web_static/releases/{}/".format(
            name.split('.')[0])
        link = "/data/web_static/current"

        if not pl.Path(a_path).is_file():
            return None

        put(a_path, '/tmp/', use_sudo=True)
        run("mkdir -p {path}".format(path=dest))
        run("tar -xzf /tmp/{name} -C {dest}"
            .format(name=name, dest=dest))
        run("rm /tmp/{name}".format(name=name))
        run("mv {dest}web_static/* {dest}"
            .format(dest=dest))
        run("rm -rf /data/web_static/current")
        run("rm -rf {dest}web_static"
            .format(dest=dest))
        run("ln -sf {dest} {link}"
            .format(dest=dest, link=link))
        return True
    except Exception:
        return False


def deploy():
    """Compress and deploy."""
    path = do_pack()
    if path:
        return do_deploy(path)
    else:
        return None
