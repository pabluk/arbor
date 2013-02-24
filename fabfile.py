from __future__ import with_statement

from fabric.api import env
from fabric.api import abort, prompt
from fabric.api import cd
from fabric.api import run, local, put


env.hosts = ['ssh.alwaysdata.com']


def deploy(version):
    """Deploy a new version using a tag as version."""
    prj_name = 'arbor-%s' % version
    pkg_name = 'arbor-%s.tar.gz' % version
    remote_dir = '/home/pabluk/www/arbor'

    # Compress, send and decompress on the remote server
    local("git archive %s --prefix=%s/ | gzip > ../%s" % (version, prj_name, pkg_name))
    put("../%s" % pkg_name, "%s/%s" % (remote_dir, pkg_name))
    with cd(remote_dir):
        run("tar xvfz %s" % pkg_name)

    env_vars = 'DJANGO_VERSION=1.4.3'

    # Replace symbolic link
    with cd(remote_dir):
        run('rm -f arbor-current')
        run('ln -s %s arbor-current' % prj_name)

    # Copy local_settings.py
    with cd(remote_dir):
        run('cp commons/local_settings.py arbor-current/arbor/')

    # Run collectstatic
    run('%s python %s/%s/manage.py collectstatic --noinput' % (env_vars, remote_dir, prj_name))


def release():
    """Release and deploy with a tag version."""
    current_branch = local('git branch | grep master', capture=True)
    if "*" not in current_branch:
        abort("Current branch isn't master.")

    latest = local("git tag | tail -n 1", capture=True)
    msg = "Enter the new version number (the last one was %s): "
    new_version = prompt(msg % latest)

    local("git tag -a -m 'Version %s' %s" % (new_version, new_version))
    deploy(new_version)
