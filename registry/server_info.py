from absl import logging
import git
import socket

def log_server_info():
    repo = git.Repo(search_parent_directories=True)
    ip = str(socket.gethostbyname_ex(socket.gethostname()))
    sha = repo.head.object.hexsha
    info = 'rev: {rev} addr: {ip}'.format(rev=sha, ip=ip)
    logging.info(info)
