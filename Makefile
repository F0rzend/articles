include .env

PYTHONPATH := ${PYTHONPATH}:$(shell pwd)/app/

default:help

help:
	@echo "Hello, world!"

alembic:
	PYTHONPATH=$(shell pwd):${PYTHONPATH} alembic ${args}

migrate:
	PYTHONPATH=$(shell pwd):${PYTHONPATH} alembic upgrade head

migration:
	PYTHONPATH=$(shell pwd):${PYTHONPATH} alembic revision --autogenerate -m "${message}"

downgrade:
	PYTHONPATH=$(shell pwd):${PYTHONPATH} alembic downgrade -1
