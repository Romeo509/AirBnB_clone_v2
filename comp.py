#!/usr/bin/python3

from fabric.api import local
from datetime import datetime


def do_pack():
    try:
        # Create the 'versions' folder if it doesn't exist
        local("mkdir -p versions")

        # Get the current date and time in the required format
        now = datetime.now()
        formatted_time = now.strftime("%Y%m%d%H%M%S")

        # Define the archive filename
        archive_filename = "web_static_{}.tgz".format(formatted_time)

        # Create the archive using tar command
        local("tar -cvzf versions/{} web_static".format(archive_filename))

        # Return the path of the generated archive
        return "versions/{}".format(archive_filename)

    except Exception as e:
        # Print an error message if an exception occurs
        print("Error: {}".format(e))
        return None
