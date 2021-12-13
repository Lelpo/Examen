export PGDATABASE := examen
export PGUSER := alumnodb
export PGPASSWORD := alumnodb
export PGCLIENTENCODING := LATIN9
export PGHOST := localhost
export DJANGOPORT := 8001
PSQL = psql
CMD = python3 manage.py
APP = examen

server:
	$(CMD) runserver $(DJANGOPORT)

reset_db: clear_db update_db create_super_user

clear_db:
	@echo Clear Database
	dropdb --if-exists $(PGDATABASE)
	createdb

poblar:
	@echo populate database
	python3 ./manage.py poblar

update_db:
	$(CMD) makemigrations $(APP)
	$(CMD) migrate

create_super_user:
	$(CMD) shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('alumnodb', 'admin@myproject.com', 'alumnodb')"


