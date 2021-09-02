build:
	docker build -t khashimoto/rmecab .
push:
	docker push khashimoto/rmecab
run:
	docker run --rm -it -v $(CURDIR):/home/mecab/ khashimoto/rmecab bash
#run:
#	docker run -d -p 8888:8888 -v $(HOME):/home/jupyter/ khashimoto/jupyterlab-minimal
