# docker-stack for BI analysis

ビジネスの分析で使うパッケージを含んだdocker images。jupyter公式のdocker-stackは全部入りで便利な反面imageサイズが1GBを越えていて、また分散処理系のパッケージなどビジネスの分析では使わないこともあるパッケージを含んでいるので出来るだけimageサイズが小さくBIの分析向きのdocker imageが欲しい。機械学習ガチ勢は素直にjupyterのdocker-stackとかgoogleのやつとか使った方が無難です

まとめると、このdocker-stackは以下の方針で作られています

- docker imageのサイズは出来るだけ小さくする
- このdocker imageはBIの分析用途

```
docker pull khashimoto/forbi:basic-alpine-m1
```

## forbi:basic(606MB)
### このimageでできること
- notebook上からathenaにクエリを打ってpandas dataframeで出力する
- pandasとmatplotlibを使った集計と可視化
- scikit-learnを使った分析
- pandas-profilingを使った探索的データ分析(alpine版のみ)

### インストール済みパッケージ
- numpy
- pandas
- matplotlib
- pyathena
- jupyter
- scikit-learn
- pyathena
- pandas-profiling(alpine版のみ)

zshrcなどで
`alias jupyter-forbi='docker run --rm -p 8888:8888 -v $HOME:/root khashimoto/forbi:basic-alpine'`
とすると便利

## forbi:time-series(650MB)

### このimageでできること
- 時系列分析

### インストール済みパッケージ
- hmmlearn
- pykalman
- statsmodels

zshrcなどで
`alias jupyter-time-series='docker run --rm -p 8888:8888 -v $HOME:/root khashimoto/forbi:time-series-alpine'`
とすると便利


## Planning
### causal-inference(coming soon)

minimalに探索的データ分析をやるpandas-profilingや統計モデリング、因果推論あたりを追加

- statsmodels
- pycausalimpact
- dowhy

### bayes(comming soon)
minimalにベイズ推論をやるパッケージを追加

- pystan
- pymc3

## ref.

- [jupyter公式のdocker-stacks](https://github.com/jupyter/docker-stacks)