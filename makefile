start:
	pip install poetry
	poetry init
install:
	poetry install --no-root
	poetry show
fastapi:
	poetry add fastapi@0.99.0
	poetry add uvicorn@0.29.0 --extras "standard"

python3:
	docker-compose exec python3 bash

mysql:
	docker-compose exec mysql bash

up:
	docker-compose build
	docker-compose up
down:
	docker-compose down
	docker builder prune