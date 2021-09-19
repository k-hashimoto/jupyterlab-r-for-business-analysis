import MeCab
 
mecab = MeCab.Tagger("-Ochasen")
sent = "このpythonスクリプトは動作確認用です"
print(mecab.parse(sent))
 
