build:
	docker build -t khashimoto/jupyterlab-slim-minimal .
	docker images | grep jupyterlab-slim-minimal
push:
	docker push khashimoto/jupyterlab-slim-minimal
run:
	docker run -d -p 8888:8888 -v $(HOME):/home/jupyter/ khashimoto/jupyterlab-slim-minimal