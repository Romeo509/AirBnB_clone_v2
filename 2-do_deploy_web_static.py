#!/usr/bin/python3
""" Fabric script that distributes archive to the
web server
"""
from fabric.api import *
from fabric.operations import *
import os
env.hosts = ['107.22.146.121', '52.91.133.213']


def do_deploy(archive_path):
    """ Return True if the operation has been correctly done
    or False if the archive_path doesn't exist
    """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        archive = archive_path.split("/")[-1]
        path = "/data/web_static/releases/{}"
        name = archive.split(".")[0]
        put(archive_path, "/tmp/{}".format(archive))
        run("rm -rf /data/web_static/releases/{}/".format(name))
        run("mkdir -p /data/web_static/releases/{}/".format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(archive, name))
        run("rm /tmp/{}".format(archive))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))
        return True
    except:
        return False
