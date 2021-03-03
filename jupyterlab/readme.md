# jupyter lab + R

## Build Docker Image
```
docker build -t khashimoto/jupyterlab.
```

## Lunch JupyterLab
```
docker run -p 8888:8888 khashimoto/jupyterlab
```