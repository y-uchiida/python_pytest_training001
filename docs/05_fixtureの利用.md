# 05 fixture の利用

fixture は、テストの前後処理を柔軟に設定するための仕組み

## fixture の基本

`import pytest` で、fixture のデコレータを読み込んで利用する

```py
import pytest


@pytest.fixture
def fixture_sample(request):

    # fixture の前処理
    print("\n ---- this is fixture_sample ---- \n")

    # 後処理は内部関数として宣言しておき、request.addfinalizer() で登録する
    def fixture_end():
        print("\n ---- this is fixture_sample end ---- \n")

    request.addfinalizer(fixture_end)


# 引数に fixture を指定する
def test_fixture_use(fixture_sample):
    print("\n start test_fixture_use() \n")
    assert True


# 引数に指定しなければfixture は適用されない
def test_without_fixture():
    print("\n start test_without_fixture() \n")
    assert True
```

上記を実行すると、以下のようになる

```bash
pytest tests/test_fixture_sample.py -sv

# ... 中略 ...

tests/test_fixture_sample.py::test_fixture_use
 ---- this is fixture_sample ----


 start test_fixture_use()

PASSED
 ---- this is fixture_sample end ----


tests/test_fixture_sample.py::test_without_fixture
 start test_without_fixture()

PASSED
```

## fixture の機能 1: スコープ

fixture 宣言時に引数として `scope` を設定すると、その fixture の適用範囲を設定できる

- scope="function" (デフォルト)
  テスト関数・メソッド単位の準備処理として、指定された関数・メソッドの前後に必ず実行される

- scope="class"
  クラス単位の fixture として、指定された fixture がクラス内で実行されていなければ実行する

- scope="module"
  モジュール単位の fixture として、指定された fixture がモジュール内で実行されていなければ実行する

## fixture の機能 2: autouse

fixture 宣言時に `autouse=True` を渡すと、個別のテスト関数の引数に fixture を指定しなくても実行する
