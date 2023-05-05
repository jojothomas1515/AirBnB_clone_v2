#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static\
folder of your AirBnB Clone repo."""
from fabric.api import run, local
import time
import pathlib as pl
import os


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
