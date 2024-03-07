#!/usr/bin/python3
""" Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers
"""
from fabric.api import *
from fabric.operations import *
import os
from datetime import datetime

env.hosts = ['107.22.146.121', '52.91.133.213']
created_path = None


def do_pack():
    """ Return an archive path """
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = "versions/web_static_{}.tgz".format(time)
    try:
        local("mkdir -p ./versions")
        local("tar --create --verbose -z --file={} ./web_static".format(file_name))
        return file_name
    except:
        return None


def do_deploy(archive_path):
    """ Return True if the operation has been correctly done
    or False if the archive_path doesn't exist
    """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        archive = archive_path.split("/")[-1]
        path = "/data/web_static/releases"
        put("{}".format(archive_path), "/tmp/{}".format(archive))
        folder = archive.split(".")
        run("mkdir -p {}/{}/".format(path, folder[0]))
        new_archive = '.'.join(folder)
        run("tar -xzf /tmp/{} -C {}/{}/"
            .format(new_archive, path, folder[0]))
        run("rm /tmp/{}".format(archive))
        run("mv {}/{}/web_static/* {}/{}/"
            .format(path, folder[0], path, folder[0]))
        run("rm -rf {}/{}/web_static".format(path, folder[0]))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/{} /data/web_static/current"
            .format(path, folder[0]))
        return True
    except:
        return False


def deploy():
    """ Creates and dixtributes an archive """
    global created_path
    if created_path is None:
        created_path = do_pack()
    return do_deploy(created_path)
