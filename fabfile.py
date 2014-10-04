# -*- coding: utf-8 -*-
#
#  fabfile.py
#  wide-language-demo
#

"""
Management commands.
"""

from fabric.api import run, cd, env, local, roles, runs_once

env.roledefs = {
    'app': [
        'direct.widelanguageindex.org',
    ],
}
env.user = 'ubuntu'
env.forward_agent = True


@runs_once
def push_code():
    local('git push')


@roles('app')
def deploy():
    push_code()
    bin_dir = '/tmp/virtualenv/widelanguagedemo/bin/'
    with cd('wide-language-demo'):
        run("git pull")
        run("git submodule init")
        run("git submodule update")
        run("{0}/pip install -r requirements.txt".format(bin_dir))
        run("kill -HUP $(cat server.pid)")
