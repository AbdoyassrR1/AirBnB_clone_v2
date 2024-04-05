#!/usr/bin/python3
""" Fabric script that creates and distributes
    archive to web_servers
"""
from fabric.api import *
import os

env.hosts = ['100.25.45.246', '18.204.11.210']
env.user = 'ubuntu'
env.key_filename = '/root/.ssh/id_rsa'


def do_clean(number=0):
    """
    Clean up old versions of web_static on both the local and remote servers.
    """
    number = int(number)
    if number < 0:
        number = 0
    elif number == 1:
        number = 2

    with lcd('versions'):
        local('ls -1t | tail -n +{} | xargs rm -rf --'.format(number + 1))

    with cd('/data/web_static/releases'):
        run('ls -1t | tail -n +{} | xargs rm -rf --'.format(number + 1))

    with cd('/data/web_static/current'):
        run('rm -rf -- {}'.format(' '.join(os.listdir('.'))))
        run('ln -s /data/web_static/releases/$(ls -1t | head -n 1) .')
