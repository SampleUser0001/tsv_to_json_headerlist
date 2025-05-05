# tsv -> json変換

- [tsv -\> json変換](#tsv---json変換)
  - [概要](#概要)
  - [実行例](#実行例)

## 概要

tsv -> json変換する。  
特定項目にフラグが立っているかを検出して、検出した場合はヘッダ行の値を取得する。

## 実行例

``` bash
python app.py testdata.tsv  | jq
```

``` json
[
  {
    "column_a": "aaa",
    "column_b": "bbb",
    "in": [
      "piyo"
    ]
  },
  {
    "column_a": "aaaa",
    "column_b": "bbbb",
    "in": [
      "hoge",
      "piyo"
    ]
  },
  {
    "column_a": "a",
    "column_b": "b",
    "in": []
  }
]

```
