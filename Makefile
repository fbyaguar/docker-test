run:
	python src/manage.py runserver 0.0.0.0:8000

install:
	pip install -r /requirements.txt

migrations:
	python src/manage.py makemigrations

showmigrations:
	python src/manage.py showmigrations

migrate:
	python src/manage.py migrate

superuser:
	python src/manage.py createsuperuser

build:
	docker-compose build

up:
	docker-compose up -d

celery:
	celery -A src worker -l info

celery-beat:
	celery -A src beat -l info

shell:
	docker exec -ti django_web /bin/bash

down:
	docker-compose down