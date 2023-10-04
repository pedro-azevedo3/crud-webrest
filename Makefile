setup:
	pip install -r requirements.txt

run: db
	python3 app.py

db:
	docker-compose up -d db