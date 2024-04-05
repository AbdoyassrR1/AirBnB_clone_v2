#!/usr/bin/python3

""" Fabric script that creates and distributes
    archives to web_servers.
"""
from fabric.api import env, put, run
import os

env.hosts = ['54.174.245.241', '54.237.92.0']


def do_deploy(archive_path):
    """
    Deploys a compressed archive to the web server.
    """
    if not os.path.exists(archive_path):
        return False

    try:

        put(archive_path, '/tmp/')

        filename = os.path.basename(archive_path)
        folder_name = '/data/web_static/releases/' + \
            os.path.splitext(filename)[0]
        run('mkdir -p {}'.format(folder_name))
        run('tar -xzf /tmp/{} -C {}'.format(filename, folder_name))

        run('rm /tmp/{}'.format(filename))

        run('mv {}/web_static/* {}'.format(folder_name, folder_name))

        run('rm -rf {}/web_static'.format(folder_name))

        run('rm -rf /data/web_static/current')

        run('ln -s {} /data/web_static/current'.format(folder_name))

        return True

    except Exception:
        return False
