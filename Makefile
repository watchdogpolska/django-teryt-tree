.PHONY: clean-pyc clean-build docs build test

clean:
	docker-compose down
	rm -r assets || true

assets:
	mkdir -p assets
	wget http://cdn.files.jawne.info.pl/public_html/2017/07/13_01_48_33/TERC.xml -O assets/TERC_old.xml
	wget http://cdn.files.jawne.info.pl/public_html/2017/07/13_01_48_33/SIMC.xml -O assets/SIMC_old.xml
	wget http://cdn.files.jawne.info.pl/public_html/2017/12/03_05_43_05/TERC_Urzedowy_2017-12-03.xml -O assets/TERC.xml
	wget http://cdn.files.jawne.info.pl/public_html/2017/12/03_05_43_05/SIMC_Urzedowy_2017-12-03.xml -O assets/SIMC.xml

build:
	docker-compose build web

test: assets
	docker-compose run -v $$PWD/assets:/assets -e CACHE_DIR=/assets/ web python manage.py test --keepdb --verbosity=2 tests.test_command.TestCommand

wait_mysql:
	docker-compose run web bash -c 'wait-for-it db:3306'

migrate:
	docker-compose run web python manage.py migrate

pyupgrade:
	docker run --rm -v $$(pwd):/data quay.io/watchdogpolska/pyupgrade

lint: pyupgrade
	docker run --rm -v $$(pwd):/apps alpine/flake8 .
	docker run --rm -v $$(pwd):/data cytopia/black --check /data

fmt:
	docker run --rm -v $$(pwd):/data cytopia/black /data

check: wait_mysql
	docker-compose run web python manage.py makemigrations --check

migrations: wait_mysql
	docker-compose run web python manage.py makemigrations

settings:
	docker-compose run web python manage.py diffsettings

docs:
	docker-compose run web sh -c 'pip install -e . && sphinx-build -b html -d docs/_build/doctrees docs docs/_build/html'
