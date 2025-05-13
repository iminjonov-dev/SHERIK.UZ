mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
create:
	python3 manage.py createsuperuser

leng:
	django-admin makemessages -l uz
	django-admin makemessages -l ru
	django-admin makemessages -l en
com:
	django-admin compilemessages
