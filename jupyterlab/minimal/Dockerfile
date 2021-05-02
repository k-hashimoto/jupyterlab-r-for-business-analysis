FROM python:3.7.10-buster
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
	&& pip install jupyterlab

RUN R -e "install.packages('devtools')" && \
R -e "devtools::install_github('IRkernel/IRkernel')" && \
R -e "IRkernel::installspec()" && \
R -e "install.packages(c('tidyverse', 'lubridate', 'httr', 'jsonlite'),  dependencies=TRUE,repos = 'http://cran.us.r-project.org')" 


WORKDIR /home/jupyter/
#start jupyterlab without password or token
RUN jupyter notebook --generate-config \
	&& echo "c.NotebookApp.token = u''" >> ~/.jupyter/jupyter_notebook_config.py \
	echo "export PATH=$PATH:/.local/bin/jupyter-notebook >> ~/.profile"
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token="]
