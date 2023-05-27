drop-db:
	flask drop-db

create-db:
	flask create-db

populate-db:
	flask populate-db

build-db:
	make -s drop-db
	make -s create-db
	make -s populate-db

run:
	gunicorn "appsilon.app:create_app()" -b 0.0.0.0:8000

test:
	pytest tests -v
	coverage report --omit="appsilon/ext/commands.py"
	coverage html
