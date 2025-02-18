COMPOSE_CMD = $(shell if docker compose version > /dev/null 2>&1; then echo "docker compose"; else echo "docker-compose"; fi)
COMPOSE_MANAGE_CMD = $(COMPOSE_CMD) run --rm django uv run manage.py

watch:
	$(COMPOSE_CMD) watch

makemigrations:
	$(COMPOSE_MANAGE_CMD) makemigrations

migrate:
	$(COMPOSE_MANAGE_CMD) migrate

createsuperuser:
	$(COMPOSE_MANAGE_CMD) createsuperuser