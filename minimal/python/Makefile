build:
	docker build -t khashimoto/jupyterlab-minimal-python:$(shell uname -m) .
push:
	docker push khashimoto/jupyterlab-minimal-python:$(shell uname -m)
run:
	docker run -d -p 8888:8888 -v $(HOME):/home/jupyter/ khashimoto/jupyterlab-minimal-python:$(shell uname -m)
