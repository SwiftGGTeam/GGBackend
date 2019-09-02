#!/bin/bash

gunicorn glaw.wsgi:application --bind 127.0.0.1:8002

NAME='glaw'
#DJANGODIR=/home/ubuntu/guardia/guardia_bk/gua
DJANGODIR=/root/GGBackend/glaw
SOCKFILE=/root/GGBackend/gunicorn.sock
USER=root # 运行此应用的用户
NUM_WORKERS=3 # gunicorn使用的工作进程数
DJANGO_SETTINGS_MODULE=glaw.settings # django的配置文件
DJANGO_WSGI_MODULE=glaw.wsgi # wsgi模块
LOG_DIR=/root/logs # 日志目录

echo "starting $NAME as `whoami`"

# 激活python虚拟运行环境
cd $DJANGODIR
source /root/.local/share/virtualenvs/GGBackend-gse_UkXO/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# 如果gunicorn.sock所在目录不存在则创建
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# 启动Django

/root/.local/share/virtualenvs/GGBackend-gse_UkXO/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
    --daemon \
    --name $NAME \
    --workers $NUM_WORKERS \
    --user=$USER --group=$GROUP \
    --log-level=debug \
    --bind=unix:$SOCKFILE \
    --access-logfile=${LOG_DIR}/gunicorn_access.log \
