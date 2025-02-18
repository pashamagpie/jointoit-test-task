# Event Management App

You can start application with Docker Compose:

```bash
docker compose watch
```

There are available:

* User registration on http://localhost:8000/api/register/

* Token obtain on http://localhost:8000/api/token/

* Token refresh on http://localhost:8000/api/token/refresh/

* CRUD (Create, Read, Update, Delete) operations & filtering with query parameters for the events on http://localhost:8000/api/events/

* Registration for specific event on http://localhost:8000/api/events/<int:event_id>/register/

* List of registrations for specific event on http://localhost:8000/api/events/<int:event_id>/registrations/

* Admin page on http://localhost:8000/admin/

* Docs on http://localhost:8000/api/schema/swagger-ui/

* Basic management commands in Makefile

Python package and environment management is implemented with [uv](https://docs.astral.sh/uv/)