# 01_pytest のインストールと実行

```bash
poetry add --group dev pytest
```

もしくは

```bash
pip install pytest
```

# テストの実行

テストの実行は, `pytest` コマンドで行う

```bash
# コマンドだけで実行しても、カレントディレクトリ配下を探してくれる
pytest

# コマンドの引数に、フォルダ名やファイル名を指定することもできる
pytest ./tests
pytest ./tests/test_sample.py

# -s オプションで、テストコマンド内で出力された内容をターミナルに表示する
# テストの挙動を確認する際に便利
pytest -s
```

pytest は、 `test_` から始まるファイルの中の、`test_` から始まる関数をテスト関数として認識して実行する  
ファイル名や関数名に `test_` がついていないと実行されないので注意
