build:
	docker build -t khashimoto/jupyterlab-trial-r .
	docker images | grep jupyterlab-trial-r
push:
	docker push khashimoto/jupyterlab-trial-r
run:
	# docker run -it --rm khashimoto/jupyterlab-trial-r R
	docker run -d -p 8888:8888 -v $(HOME):/home/jupyter/ khashimoto/jupyterlab-trial-r