#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['3.80.116.142', '34.203.212.217']


def do_pack():
    """generates a tgz archive"""
    try:
        if os.path.isdir("versions") is False:
            local("mkdir -p versions")

        targz_file_name = "versions/web_static_{}.tgz".format(
            datetime.now().strftime("%Y%m%d%H%M%S"))

        result = local("tar -cvzf {} web_static".format(targz_file_name))
        return result
    except Exception:
        return None


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        file_not_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run("mkdir -p {}{}".format(path, file_not_ext))
        run("tar xzf /tmp/{} -C {}{}/".format(file_name, path, file_not_ext))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, file_not_ext))
        run("rm /tmp/{}".format(file_name))
        run("rm /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, file_not_ext))
        return True
    except Exception:
        return False


def deploy():
    """ deploy """
    pack = do_pack()
    if pack is None:
        return False
    return do_deploy(pack)
