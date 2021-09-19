FROM python:3.8.11-slim-bullseye

RUN apt-get update && apt-get install -y \
	make \
	curl \
	file \
	git \
	xz-utils \
	libmecab-dev \
	mecab \
	mecab-ipadic-utf8 \
	sudo

RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git && \
	mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -y

WORKDIR /root
ADD requirements.txt /root
RUN pip install -r requirements.txt
WORKDIR /home/mecab
