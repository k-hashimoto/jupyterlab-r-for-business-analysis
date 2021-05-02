FROM khashimoto/jupyterlab-minimal
RUN apt install libv8-dev -y
RUN R -e "install.packages(c('rstan','bayesplot', 'ggfortify', 'gridExtra'), dependencies=TRUE,repos = 'http://cloud.r-project.org/')" 

#WORKDIR /home/jupyter/
##start jupyterlab without password or token
#RUN jupyter notebook --generate-config \
#	&& echo "c.NotebookApp.token = u''" >> ~/.jupyter/jupyter_notebook_config.py \
#	echo "export PATH=$PATH:/.local/bin/jupyter-notebook >> ~/.profile"
#CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token="]
