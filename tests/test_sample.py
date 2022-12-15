# テストの実行は、 pytest コマンドで行う
# コマンドだけで実行しても、tests ディレクトリ配下を探してくれる
# コマンドの引数に、フォルダ名やファイル名を指定することもできる

# pytest は、 test_ から始まるファイルの中の、
# test_ から始まる関数をテスト関数として認識して実行する
# ファイル名や関数名に test_ がついていないと実行されないので注意

# -s オプションで、テストコマンド内で出力された内容をターミナルに表示する
# テストの挙動を確認する際に便利

# 1. 何もしないテスト
def test_hello_world():
    print("hello world")


def test_assertの実行_Trueの場合():
    # assert は、結果が True の場合にテストをPassさせる
    assert 1 == 1


def test_assertの実行_Falseの場合():
    # 結果が False になるテストはFail になる
    assert (1 + 1) == 3


def test_assertで暗黙的な真偽値変換を検証する_Trueの場合():
    assert "a"


def test_assertで暗黙的な真偽値変換を検証する_Falseの場合():
    assert None
