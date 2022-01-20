# Unvail PDF Masking

授業用途などで文字列がマスキングされたpdfファイルのマスキングを剥がしているように見えるスクリプトです。

## 使い方
```
$ ./unvail-pdf.py -i INPUT -o OUTPUT
```

## しくみ
元のpdfから画像をすべて取り除いたpdfを作成し、それを元のpdfの上に重ねる。よってファイルサイズが最悪の場合2倍になる。

## 注意
- 文字情報がpdfファイルに残っていないときは動作しません。(画像化されていたり)
- マスキングの色が文字色と同じ色だと結局見えないままかも