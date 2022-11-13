PHONY: build
build:
	docker-compose build

PHONY: up
up:
	docker-compose up

PHONY: logs
logs:
	docker-compose logs -f --tail=100

PHONY: bash
bash:
	docker-compose run --rm app /bin/sh

PHONY: lint
lint:
	docker-compose run --rm app pylint --load-plugins pylint_flask /app

PHONY: test
test:
	docker-compose run --rm app pytest -vvv --cov=.

PHONY: down
down:
	docker-compose down --remove-orphans
