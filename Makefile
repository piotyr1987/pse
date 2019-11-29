build:
	@docker-compose build

start:
	@docker-compose up -d

stop:
	@docker-compose stop

test:
	@docker-compose run --rm web coverage run manage.py test -v 2

report:
	@docker-compose run --rm web coverage report

migrate:
	@docker-compose run --rm web python manage.py migrate

import:
	@docker-compose run --rm web python manage.py import_packages_list
