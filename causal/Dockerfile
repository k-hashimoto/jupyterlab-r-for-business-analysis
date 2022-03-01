FROM khashimoto/jupyterlab-minimal
RUN R -e "install.packages(c('MatchIt'), dependencies=TRUE,repos = 'http://cloud.r-project.org/')"

#WORKDIR /home/jupyter/
##start jupyterlab without password or token
#RUN jupyter notebook --generate-config \
#	&& echo "c.NotebookApp.token = u''" >> ~/.jupyter/jupyter_notebook_config.py \
#	echo "export PATH=$PATH:/.local/bin/jupyter-notebook >> ~/.profile"
#CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token="]
