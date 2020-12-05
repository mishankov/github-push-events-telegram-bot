run:
	gunicorn main:app -k uvicorn.workers.UvicornWorker
push-all:
ifdef m
	black .
	git add .
	git commit -m "${m}"
	git push
endif
