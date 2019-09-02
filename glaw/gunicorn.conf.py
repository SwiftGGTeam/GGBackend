import multiprocessing

bind = '127.0.0.1:8000'
workers = 2
errorlog = '/root/logs/gunicorn.error.log' #发生错误时log的路径
accesslog = '/root/logs/gunicorn.access.log' #正常时的log路径
#loglevel = 'debug'   #日志等级
proc_name = 'ggbackend'   #进程名

