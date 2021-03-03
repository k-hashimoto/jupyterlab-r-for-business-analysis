FROM python:3.9.2-buster
RUN apt-get update -qq && apt-get install -y git-core \
	libssl-dev \
	libssl-dev curl libcurl4-openssl-dev \
	curl \
	libxml2-dev \
	libssl-dev \
	make

RUN MAKE='make -j 25' && apt-get install -y r-base \
	&& pip install jupyter \
	&& pip install jupyterlab    

RUN apt install libgit2-dev -y
#install this package
#RUN R -e "if (!require('devtools')) install.packages('devtools',  dependencies=TRUE,repos = 'http://cran.us.r-project.org')"
RUN R -e "install.packages('devtools')"
RUN	R -e "devtools::install_github('IRkernel/IRkernel')" 
RUN	R -e "IRkernel::installspec()" 
RUN	R -e "install.packages(c('caret', 'dplyr', 'randomForest', 'lubridate', 'httr', 'jsonlite','h2o'),  dependencies=TRUE,repos = 'http://cran.us.r-project.org')" 
  
# install java
RUN apt update && apt-get install -y default-jdk

#start jupyterlab without password or token
RUN jupyter notebook --generate-config \
	&& echo "c.NotebookApp.token = u''" >> ~/.jupyter/jupyter_notebook_config.py \
	echo "export PATH=$PATH:/.local/bin/jupyter-notebook >> ~/.profile"
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token="]    