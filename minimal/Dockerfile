FROM python:3.8.11-slim-bullseye
RUN apt-get clean && \
	apt-get update && \
	apt-get install -y \
	libssl-dev \
	libcurl4-openssl-dev \
	libxml2-dev \
	libssl-dev \
	libgit2-dev \
	git-core \
	default-jdk \
	curl \
	make \
	r-base \
	fonts-ipaexfont \
	fonts-noto-cjk \
	locales && locale-gen ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL=ja_JP.UTF-8
RUN localedef -f UTF-8 -i ja_JP ja_JP.utf8

RUN MAKE='make -j 25'  \
	pip install jupyter \
	&& pip install jupyterlab \
	&& pip install numpy pandas matplotlib

RUN R -e "install.packages('devtools')" && \
R -e "devtools::install_github('IRkernel/IRkernel')" && \
R -e "IRkernel::installspec()" && \
R -e "install.packages(c('tidyverse', 'lubridate', 'httr', 'jsonlite', 'tidylog','gtsummary'),  dependencies=TRUE, repos = 'http://cran.us.r-project.org')"

WORKDIR /home/jupyter/

#start jupyterlab without password or token
RUN jupyter notebook --generate-config \
	&& echo "c.NotebookApp.token = u''" >> ~/.jupyter/jupyter_notebook_config.py \
	echo "export PATH=$PATH:/.local/bin/jupyter-notebook >> ~/.profile"
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token="]
