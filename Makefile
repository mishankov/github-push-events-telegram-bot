install:
	python3 -m venv venv
	. venv/bin/activate
	pip3 install --upgrade pip
	pip3 install -r requirements.txt

run:
	. venv/bin/activate
	gunicorn --chdir src main:app -k uvicorn.workers.UvicornWorker

commit-all:
ifdef m
	black .
	git add .
	git commit -m "${m}"
endif

push-all:
ifdef m
	black .
	git add .
	git commit -m "${m}"
	git push
endif
