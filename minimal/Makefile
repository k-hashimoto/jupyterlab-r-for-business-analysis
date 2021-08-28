build:
	docker build -t khashimoto/jupyterlab-minimal .
push:
	docker push khashimoto/jupyterlab-minimal
run:
	docker run -d -p 8888:8888 -v $(HOME):/home/jupyter/ khashimoto/jupyterlab-minimal