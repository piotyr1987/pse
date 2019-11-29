
# PSE

It downloads a list of new packages from https://pypi.org/rss/packages.xml once a day.

## Getting Started

Clone the repository

git clone https://github.com/piotyr1987/pse.git

cd pse

You can set number of packages on the site in env file.

PAGINATION_PAGE_SIZE = 5 - default value

### Prerequisites

Running the project requires installation of the docker and docker-compose

### Installing

If you are using Linux or MacOS you can use make commands:

make build

make migrate

make start

make import

In other OS use:

docker-compose build

docker-compose run --rm web python manage.py migrate

docker-compose up -d

docker-compose run --rm web python manage.py import_packages_list

Access to the packets search engine:
http://127.0.0.1:8000/

Access to the API
http://127.0.0.1:8000/api/pypi/q=

## Running the tests

Linux and MacOS

make test

make report

Other OS

docker-compose run --rm web coverage run manage.py test

docker-compose run --rm web coverage report
