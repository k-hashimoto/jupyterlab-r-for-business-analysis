# jupyterlab + R for business analysis

This repository is for docker image which contain jupyterlab and R

## jupyterlab

### minimal

minimal image for R and python with jupyterlab

*deploy on local*

```
docker pull khashimoto/jupyterlab-minimal
```

*installed packages for R*

- tidyverse
- tidylog
- lubridate
- httr
- jsonlite
- gtsummary

*installed packages for python*

- numpy
- pandas
- matplotlib

### bayes

for bayes analysis

*deploy on local*

```
docker pull khashimoto/jupyterlab-bayes
```

*installed packages for R*

- (packages in minimal)
- rstan
- bayesplot
- ggfortify
- gridExtra

*run jupyterLab*
```
docker run -d -p 8888:8888 -v `pwd`:/home/jupyter/ khashimoto/jupyterlab-minimal
```

## slim
low size images
