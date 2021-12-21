FROM khashimoto/jupyterlab-minimal-base

WORKDIR /root
ADD requirements.txt /root
RUN pip install -r requirements.txt
WORKDIR /home/jupyter/

# start jupyterlab without password or token
RUN jupyter notebook --generate-config \
	&& echo "c.NotebookApp.token = u''" >> ~/.jupyter/jupyter_notebook_config.py \
	echo "export PATH=$PATH:/.local/bin/jupyter-notebook >> ~/.profile"

# custum settings
# 1. show line number as default
# 2. change terminal font
RUN mkdir -p ~/.jupyter/lab/user-settings/@jupyterlab/notebook-extension && \
	echo '{"codeCellConfig": {"lineNumbers": true}}' > \
  	~/.jupyter/lab/user-settings/@jupyterlab/notebook-extension/tracker.jupyterlab-settings && \
	mkdir -p ~/.jupyter/lab/user-settings/@jupyterlab/terminal-extension/ && \
	echo '{"fontFamily": "Monaco"}' > \
	~/.jupyter/lab/user-settings/@jupyterlab/terminal-extension/plugin.jupyterllsab-settings

# enable dark mode
# if you want swich dark mode, erase these comment out and build image.
# RUN mkdir -p ~/.jupyter/lab/user-settings/@jupyterlab/apputils-extension && \
# 	echo '{"theme":"JupyterLab Dark"}' > \
#   	~/.jupyter/lab/user-settings/@jupyterlab/apputils-extension/themes.jupyterlab-settings

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token="]
