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


## slim-stack

alipe based very low size images. see readme
