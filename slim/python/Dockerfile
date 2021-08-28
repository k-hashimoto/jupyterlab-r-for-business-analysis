FROM python:3.7-slim AS compile-image
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc

RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.7-slim AS build-image
COPY --from=compile-image /opt/venv /opt/venv

WORKDIR /home/jupyter/

#start jupyterlab without password or token
ENV PATH="/opt/venv/bin:$PATH"
RUN jupyter notebook --generate-config \
	&& echo "c.NotebookApp.token = u''" >> ~/.jupyter/jupyter_notebook_config.py \
	echo "export PATH=$PATH:/.local/bin/jupyter-notebook >> ~/.profile"

# show line number as default
RUN  mkdir -p ~/.jupyter/lab/user-settings/@jupyterlab/notebook-extension && \
	echo '{"codeCellConfig": {"lineNumbers": true}}' > \
  	~/.jupyter/lab/user-settings/@jupyterlab/notebook-extension/tracker.jupyterlab-settings

# enable dark mode
# if you want swich dark mode, erase these comment out and build image.
# RUN mkdir -p ~/.jupyter/lab/user-settings/@jupyterlab/apputils-extension && \
# 	echo '{"theme":"JupyterLab Dark"}' > \
#   	~/.jupyter/lab/user-settings/@jupyterlab/apputils-extension/themes.jupyterlab-settings

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token="]
