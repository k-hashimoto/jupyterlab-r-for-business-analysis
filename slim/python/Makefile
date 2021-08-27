build:
	docker build -t khashimoto/jupyterlab-trial-python .
	docker images | grep jupyterlab-trial-python
push:
	docker push khashimoto/jupyterlab-trial-python
run:
	docker run -d -p 8888:8888 -v $(HOME):/home/jupyter/ khashimoto/jupyterlab-trial-python