from tljh.hooks import hookimpl
from tljh.user import ensure_group
import sh

@hookimpl
def tljh_extra_user_conda_packages():
    return ['voila']

@hookimpl
def tljh_config_post_install(config):
    """
    Configure /srv/shared_folders and change configs/mods
    """
    sh.mkdir('/srv/shared_folders', '-p')
    # jupyterhub-users doesn't get created until a user logs in
    # make sure it's created before changing permissions on directory
    ensure_group('jupyterhub-users') 
    sh.chown('root:jupyterhub-users', '/srv/shared_folders')
    sh.chmod('777', '/srv/shared_folders')
    sh.chmod('g+s', '/srv/shared_folders')
    sh.ln('-s', '/srv/shared_folders', '/etc/skel/shared_folders')

    
    
    