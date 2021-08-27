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
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token="]
