release: cd executivetable_restserver && python3 manage.py makemigrations && python3 manage.py migrate
web: gunicorn executivetable_restserver.wsgi --log-file -