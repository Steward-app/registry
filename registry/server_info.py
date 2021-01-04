from absl import logging
import socket
import registry

def log_server_info():
    ip = str(socket.gethostbyname_ex(socket.gethostname()))
    info = 'version: {version} addr: {ip}'.format(version=registry.__version__, ip=ip)
    logging.info(info)
