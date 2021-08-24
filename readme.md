# Docker images for business analysis

## jupyterlab

### minimal

minimal image for R and python with jupyterlab

*deploy on local*

```
docker pull khashimoto/jupyterlab-minimal
```

*installed packages for R*

- tidyverse
- lubridate
- httr
- jsonlite
- data.tree
- gtsummary

*installed packages for python*

- numpy
- pandas

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


## slim-stack

alipe based very low size images. see readme
