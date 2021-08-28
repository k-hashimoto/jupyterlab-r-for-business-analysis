build:
	docker build -t khashimoto/jupyterlab-python-slim-minimal .
	docker images | grep jupyterlab-python-slim-minimal
push:
	docker push khashimoto/jupyterlab-python-slim-minimal
run:
	docker run -d -p 8888:8888 -v $(HOME):/home/jupyter/ khashimoto/jupyterlab-python-slim-minimal