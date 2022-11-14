PHONY: build
build:
	docker-compose build

PHONY: up
up: build
	docker-compose up

PHONY: lint
lint:
	docker-compose run --rm app pylint --load-plugins pylint_flask /app

PHONY: test
test:
	docker-compose run --rm app pytest -vvv --cov=.
