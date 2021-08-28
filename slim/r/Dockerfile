FROM python:3.7-slim AS compile-image
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc \
	libssl-dev \
	libcurl4-openssl-dev \
	libxml2-dev \
	libssl-dev \
	libgit2-dev \
	git-core \
	default-jdk \
	curl \
	r-base

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN R -e "install.packages('devtools')" && \
	R -e "install.packages('IRkernel')" && \
	# R -e "devtools::install_github('IRkernel/IRkernel')" && \
	R -e "IRkernel::installspec()" && \
	R -e "install.packages(c('tidyverse', 'lubridate', 'httr', 'jsonlite', 'tidylog','gtsummary'),  dependencies=TRUE, repos = 'http://cran.us.r-project.org')"


FROM python:3.7-slim AS build-image
RUN apt-get update && \
	apt-get install -y --no-install-recommends \
	r-base \
	libxml2-dev \
	locales && locale-gen ja_JP.UTF-8

ENV PATH="/opt/venv/bin:$PATH"
COPY --from=compile-image /opt/venv /opt/venv
COPY --from=compile-image /usr/local/lib/R/site-library /usr/local/lib/R/site-library
COPY --from=compile-image /usr/lib/R/site-library /usr/lib/R/site-library
COPY --from=compile-image /usr/lib/R/library /usr/lib/R/library

RUN	R -e "install.packages('IRkernel')" && \
	R -e "IRkernel::installspec()"

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL=ja_JP.UTF-8
RUN localedef -f UTF-8 -i ja_JP ja_JP.utf8
WORKDIR /home/jupyter/

#start jupyterlab without password or token

RUN jupyter notebook --generate-config \
	&& echo "c.NotebookApp.token = u''" >> ~/.jupyter/jupyter_notebook_config.py \
	echo "export PATH=$PATH:/.local/bin/jupyter-notebook >> ~/.profile"
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token="]
