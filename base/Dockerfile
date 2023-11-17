FROM python:3.11.3-slim-bullseye
RUN apt-get clean && \
	apt-get update && \
	apt-get install -y \
	libssl-dev \
	libcurl4-openssl-dev \
	libxml2-dev \
	libssl-dev \
	libgit2-dev \
	libgomp1 \
	git-core \
	default-jdk \
	curl \
	make \
	git \
	fonts-ipaexfont \
	fonts-noto-cjk \
	gcc \
	locales && locale-gen ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL=ja_JP.UTF-8
RUN localedef -f UTF-8 -i ja_JP ja_JP.utf8
