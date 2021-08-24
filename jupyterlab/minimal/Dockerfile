FROM python:3.8.11-bullseye
RUN apt-get clean && \
	apt-get update && \
	apt-get install -y git-core \
	libssl-dev \
	libssl-dev curl libcurl4-openssl-dev \
	curl \
	libxml2-dev \
	libssl-dev \
	make \
	libgit2-dev \
	default-jdk

RUN MAKE='make -j 25' && apt-get install -y r-base \
	&& pip install jupyter \
	&& pip install jupyterlab \
	&& pip install numpy pandas

RUN R -e "install.packages('devtools')" && \
R -e "devtools::install_github('IRkernel/IRkernel')" && \
R -e "IRkernel::installspec()" && \
R -e "install.packages(c('tidyverse', 'lubridate', 'httr', 'jsonlite', 'data.tree','gtsummary'),  dependencies=TRUE,repos = 'http://cran.us.r-project.org')"

RUN apt-get update \
    && apt-get install -y locales \
    && locale-gen ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL=ja_JP.UTF-8
RUN localedef -f UTF-8 -i ja_JP ja_JP.utf8

# 日本語フォントをインストール
RUN apt-get update && apt-get install -y \
  fonts-ipaexfont \
	fonts-noto-cjk

WORKDIR /home/jupyter/

#start jupyterlab without password or token
RUN jupyter notebook --generate-config \
	&& echo "c.NotebookApp.token = u''" >> ~/.jupyter/jupyter_notebook_config.py \
	echo "export PATH=$PATH:/.local/bin/jupyter-notebook >> ~/.profile"
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token="]
