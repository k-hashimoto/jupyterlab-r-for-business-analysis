# forbi:basic-alpine

以下の理由からalpineを採用しています

- 探索的データ分析を行うpandas-proflingはLLVMの最近のバージョンを要求していますが、debian-busterベースのpython3.X系列のdocker imageにこれを入れるのが面倒。それに対してalpineは簡単だった。
- docker imageのサイズ削減

ただalpineを採用したためかimageのbuild時間が超長くなっています。`forbi:basic-alpine` をMacBookAir(M1,2020)でbuildすると46分もかかります。
```
[base 3/4] RUN pip install --user   numpy  scipy  scikit-learn  matplotlib  pandas  pyathena  jupyter         2872.0s
```
パッケージ追加のためにDockerfileを編集する際は新しく `RUN pip install --user XXXX` の行を追加した方が良いです。

