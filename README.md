# django_celery

# запуск Redis
redis-server

# запуск Celery
celery -A django_celery worker -P gevent --loglevel=info