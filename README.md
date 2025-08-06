# django_celery

# запуск Redis (брокер сообщений)
redis-server

# запуск Celery (выполнение задач в фоновом режиме)
celery -A django_celery worker -P gevent --loglevel=info

# запуск Celery Beat (для переодических задач)
celery -A django_celery beat

# запуск Flower (веб-инструмент для отслеживания работы Celery.)
celery -A django_celery flower