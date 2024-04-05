#!/usr/bin/python3

"""
fabric script that create a .tgz archive from
the conten of the web_static folder.
"""
from fabric.api import lacal
from datetime import datetime

def do_pack():
    """
    Compresse content of the web_static folder into a .tgz.
    Returns:
            The path to the generated archive
            None otherwise.
    """
    try:
        now = datetime.now()
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second)
        local("sudo mkdir -p versions")
        local("sudo tar -czvf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except Exception:
        return None
