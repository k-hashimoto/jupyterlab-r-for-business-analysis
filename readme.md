# docker-stack for BI analysis

ビジネスの分析で使うパッケージを含んだdocker images。jupyter公式のdocker-stackは全部入りで便利な反面imageサイズが大きくまた分散処理系のパッケージなどビジネスの分析では使わないこともあるパッケージを含んでいるので出来るだけimageサイズが小さくBIの分析向きのdocker imageが欲しい。機械学習ガチ勢とかは素直にjupyterのdocker-stackとかgoogleのやつとか使った方が無難です

したがって、このdocker-stackは以下の方針で作られています

- imageサイズは出来るだけ小さくする
- このnotebookはBIの分析用途

## basic
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
`alias jupyter-minimal='docker run --rm -p 8888:8888 -v $HOME:/root forbi:basic-alpine'`
とすると便利

## time-series(coming soon)

minimalに時系列分析系ライブラリを追加

- hmmlearn
- pykalman
- statsmodels

## causal-inference(coming soon)

minimalに探索的データ分析をやるpandas-profilingや統計モデリング、因果推論あたりを追加

- statsmodels
- pycausalimpact
- dowhy

## bayes(comming soon)
minimalにベイズ推論をやるパッケージを追加

- pystan
- pymc3


## ref.

- [jupyter公式のdocker-stacks](https://github.com/jupyter/docker-stacks)