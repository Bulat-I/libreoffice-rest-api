import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

PORT = os.getenv("PORT", 2002)
backlog = os.getenv("BACKLOG", 64)
timeout = os.getenv("TIMEOUT", 4)
workers = os.getenv("WORKERS", 1)
worker_connections = os.getenv("WORKER_CONNECTIONS", 100)
keepalive = os.getenv("KEEPALIVE", 2)

bind = f'0.0.0.0:{PORT}'
worker_class = 'sync'
spew = False
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None
errorlog = '-'
loglevel = 'debug'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
proc_name = None
