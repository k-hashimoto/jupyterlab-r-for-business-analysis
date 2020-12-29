FROM python:3.8-alpine as base
RUN apk update
RUN apk --update-cache add \
	gcc \
	g++ \
#	llvm \
#	zeromq-dev \
#	libffi-dev \
#	lapack-dev \
	openblas-dev \
	gfortran \
	musl
RUN apk --update-cache add python3-dev
RUN pip install --upgrade pip  
RUN pip install --user numpy
RUN pip install --user scipy 
RUN apk --update-cache add libffi-dev lapack-dev zeromq-dev llvm
RUN apk add zlib
RUN pip install --user scikit-learn 
RUN apk add zlib-dev jpeg-dev make
RUN pip install --user matplotlib

RUN pip install --user pandas

RUN pip install --user pyathena

RUN pip install --user jupyter
# RUN pip install --user \
# 	numpy==1.14.5 \
# 	pandas \
# 	jupyter \
# 	matplotlib \
# 	seaborn \
# 	pyathena \
# 	scikit-learn

# FROM python:3.8-alpine as app
# RUN apk update
# RUN apk add \
# 	zeromq-dev \
# 	libffi-dev \
# 	lapack-dev \
# 	openblas-dev

RUN apk add llvm-dev
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

