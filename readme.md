# jupyterlab + R for business analysis

This repository is for docker image which contain jupyterlab and R

## jupyterlab

### minimal

minimal image for R and python with jupyterlab

*deploy on local*

```
intel mac => docker pull khashimoto/jupyterlab-minimal:x86_64
m1 mac => pull khashimoto/jupyterlab-minimal:arm64
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


```
intel mac => docker run -d -p 8888:8888 -v $HOME:/home/jupyter khashimoto/jupyterlab-minimal:x86_64
m1 mac => docker run -d -p 8888:8888 -v $HOME:/home/jupyter khashimoto/jupyterlab-minimal:arm64

```

### minimal-python

minimal image for python with jupyterlab(without R kernel)

*installed packages for python*

- jupyterlab
- numpy
- pandas
- matplotlib
- seaborn
- jupyterlab-git
- scikit-learn

```
intel mac => docker run -d -p 8888:8888 -v $HOME:/home/jupyter khashimoto/jupyterlab-minimal-python:x86_64
m1 mac => docker run -d -p 8888:8888 -v $HOME:/home/jupyter khashimoto/jupyterlab-minimal-python:arm64

```

### kaggle

minimal image for kaggle.

*installed packages*
- (packages in minimal)
- kaggle cli
- seaborn
- lightgbm
- scikit-learn

*deploy on local*
```
intel mac => docker pull khashimoto/jupyterlab-kaggle:x86_64
m1 mac => docker pull khashimoto/jupyterlab-kaggle:arm64

```

*run jupyterLab*

```
intel mac => docker run -d -p 8888:8888 -v $HOME:/home/jupyter khashimoto/jupyterlab-kaggle:x86_64
m1 mac => docker run -d -p 8888:8888 -v $HOME:/home/jupyter khashimoto/jupyterlab-kaggle:arm64
```

### causal

for causal inference

*installed packages for R*

- MatchIt


### bayes

for bayes analysis

*deploy on local*

```
intel mac => docker pull khashimoto/jupyterlab-bayes:x86_64
m1 mac => pull khashimoto/jupyterlab-bayes:arm64
```

*installed packages for R*

- (packages in minimal)
- rstan
- bayesplot
- ggfortify
- gridExtra


## options

### line number

As default, line number of notebook is enabled.

### dark mode

if you want to enable dark mode forever, erase comment out at end of minimal/Dockerfile and rebuild image.
