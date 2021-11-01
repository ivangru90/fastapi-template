.PHONY: clean system-packages python-packages install tests run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

system-packages:
	sudo apt install python-pip -y

python-packages:
	pip install -r requirements.txt

install: system-packages python-packages

tests:
	python manage.py test

run:
	uvicorn app.main:app --host 0.0.0.0 --port 5000

all: clean install tests run
