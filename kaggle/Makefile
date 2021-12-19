build:
	docker build -t khashimoto/jupyterlab-kaggle:$(shell uname -m) .
push:
	docker push khashimoto/jupyterlab-kaggle:$(shell uname -m)
run:
	docker run -d -p 8888:8888 -v $(HOME):/home/jupyter khashimoto/jupyterlab-kaggle:$(shell uname -m)
