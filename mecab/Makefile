build:
	docker build -t khashimoto/mecab-python .
push:
	docker push khashimoto/mecab-python
run:
	docker run --rm -it -v $(CURDIR):/home/mecab/ khashimoto/mecab-python bash
