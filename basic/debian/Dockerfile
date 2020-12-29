FROM build-base:slim as builder
FROM python:3.8.7-slim-buster as base
ARG NB_USER="analyzer"
ARG NB_PASSWORD=analyzer
ARG NB_UID="1000"
ARG NB_GID="100"

ENV NB_USER=$NB_USER \
    NB_UID=$NB_UID \
	NB_GID=$NB_GID \
	NB_PASSWORD=$NB_PASSWORD

RUN useradd -m --uid ${NB_UID} --groups sudo ${NB_USER} \
 	&& echo ${NB_USER}:${NB_PASSWORD} | chpasswd
USER $NB_UID

COPY --from=builder /home/analyzer/.local/bin /usr/local/bin
COPY --from=builder /home/analyzer/.local/etc /usr/local/etc
COPY --from=builder /home/analyzer/.local/share /usr/local/share
COPY --from=builder /home/analyzer/.local/lib /usr/local/lib
ENV PATH=/usr/local/bin:$PATH

COPY --from=builder /usr/local/etc/jupyter/jupyter_notebook_config.py /usr/local/etc/jupyter/
ENV JUPYTER_CONFIG_DIR=/usr/local/etc/jupyter

WORKDIR /home/analyzer
EXPOSE 8888
CMD ["jupyter","notebook"]

# todo
# pandasの日本語対策
# https://qiita.com/yubiquita/items/9c056e175ccb085eb137
