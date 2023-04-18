FROM jupyter/r-notebook
# RUN R -e "install.packages('shinystan')"
# RUN R -e "install.packages('rstan', repos = 'https://cloud.r-project.org/', dependencies=TRUE)"
# RUN R -e "install.packages('rstan', repos = c('https://mc-stan.org/r-packages/', getOption('repos'), dependencies=TRUE))"

#RUN R -e "install.packages(c('rstan'), dependencies=TRUE,repos = 'http://cloud.r-project.org/')"
RUN R -e "install.packages(c('rstan','bayesplot', 'ggfortify', 'gridExtra'), dependencies=TRUE,repos = 'http://cloud.r-project.org/')"

#WORKDIR /home/jupyter/
##start jupyterlab without password or token
#RUN jupyter notebook --generate-config \
#	&& echo "c.NotebookApp.token = u''" >> ~/.jupyter/jupyter_notebook_config.py \
#	echo "export PATH=$PATH:/.local/bin/jupyter-notebook >> ~/.profile"
#CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token="]
