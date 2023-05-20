#!/usr/bin/python3

from fabric.api import sudo, put, env, run

env.hosts = ['34.205.65.154', '34.239.107.150']
env.user = 'ubuntu'

def do_clean():
    """Wipes both web servers."""
    res = put("clean_server.sh", "~/", mode="777")
    try:
        sudo("./clean_server.sh")
    except Exception:
        return False
    return True

def do_setup():
    """Setup the web server with task on requirements."""
    try:
        put("0-setup_web_static.sh", "~/", mode="777")
        run("sudo ./0-setup_web_static.sh")
        return True
    except Exception:
        return False
