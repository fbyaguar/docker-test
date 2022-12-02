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
	docker-compose --env-file ./.env up -d

shell:
	docker exec -ti test-drf_web_1 /bin/bash

down:
	docker-compose down