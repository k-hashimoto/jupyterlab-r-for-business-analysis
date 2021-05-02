# jupyter lab + R

## Pull Docker image
```
docker pull khashimoto/jupyterlab-minimal
```
```
docker pull khashimoto/jupyterlab-bayes
```

## Build Docker Image
```
docker build -t khashimoto/jupyterlab-minimal .
```

## Lunch JupyterLab
```
docker run -d -p 8888:8888 -v `pwd`:/home/jupyter/ khashimoto/jupyterlab-minimal
```
