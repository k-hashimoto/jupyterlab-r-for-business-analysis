# jupyter lab + R

## Build Docker Image
```
docker build -t khashimoto/jupyterlab.
```

## Lunch JupyterLab
```
docker run -d -p 8888:8888 -v `pwd`:/home/jupyter/ khashimoto/jupyterlab
```