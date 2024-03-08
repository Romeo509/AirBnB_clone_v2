#!/usr/bin/python3
""" Develop a Fabric script featuring the 'do_pack' function to create
a .tgz archive from 'web_static' in your AirBnB Clone repo.
The archive, named 'web_static_<timestamp>.tgz',is stored in the
'versions' folder. 'do_pack' returns the archive path on success,
or None on failure.
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """ Return the archive path """
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = "versions/web_static_{}.tgz".format(time)
    try:
        local("mkdir -p ./versions")
        local("tar --create --verbose -z --file={} ./web_static"
              .format(file_name))
        return file_name
    except:
        return None
