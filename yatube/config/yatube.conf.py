[program:cms]
command=/home/USER/venv/bin/gunicorn config.wsgi:application -c /home/USER/CMS/config/gunicorn.conf.py
directory = /home/USER/CMS
user = USER
autorestart=true
redirect_stderr=true
stdout_logfile = /home/USER/CMS/logs/debug.log