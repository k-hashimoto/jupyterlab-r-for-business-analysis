FROM forbi-build-deps:alpine as base
RUN pip install --upgrade pip
RUN pip install --user  \
	numpy \
	scipy \
	scikit-learn \
	matplotlib \
	pandas \
	pyathena \
	jupyter
RUN pip install --user pandas-profiling[notebook]

FROM python:3.8-alpine as app
RUN apk add zeromq openblas jpeg llvm-dev
COPY jupyter_notebook_config.py /usr/etc/jupyter/.jupyter/
COPY --from=base /root/.local/bin   /usr/local/bin
COPY --from=base /root/.local/etc   /usr/local/etc
COPY --from=base /root/.local/share /usr/local/share
COPY --from=base /root/.local/lib   /usr/local/lib
ENV PATH=/usr/local/bin:$PATH

WORKDIR /root
EXPOSE 8888
ENV JUPYTER_CONFIG_DIR=/usr/etc/jupyter/.jupyter
CMD ["jupyter","notebook","--allow-root"]

