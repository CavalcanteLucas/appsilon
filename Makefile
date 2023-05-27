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
	flask run
