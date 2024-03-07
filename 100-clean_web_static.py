#!/usr/bin/python3
""" Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives, using the function do_clean
"""

import os
from fabric.api import *

env.hosts = ['107.22.146.121', '52.91.133.213']


def do_clean(number=0):
    """ Deletes out-of-date archive
    If number is 0 or 1, keep only the most recent archive
    If number is 2, kepp the most and second-most recent archives
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(arch)) for arch in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [arch for arch in archives if "web_static_" in arch]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(arch)) for arch in archives]
