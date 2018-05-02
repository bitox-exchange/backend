all: build restart

restart:
	docker-compose kill && docker-compose rm -vf && docker-compose up -d

build:
	docker-compose build

logs:
	docker-compose logs -f
