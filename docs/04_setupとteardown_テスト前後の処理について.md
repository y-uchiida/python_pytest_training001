# 04 setup と teardown テスト前後の処理について

`setup_function` は、それぞれのテスト関数の実行前に処理される  
`teardown_function` は、それぞれのテスト関数の実行後に処理される

テストの共通処理（フレームワークやライブラリのセットアップ、テストデータの読み込みなど）を記述すると便利

## テスト関数に対する前後処理

```py
# テストの前処理と後処理

# テスト関数を実行する前に処理されるsetup_function
def setup_function(function):
    print("\n --- setup function start --- \n")


# テスト関数が完了した後に処理されるteardown_function
def teardown_function(function):
    print("\n --- teardown function start --- \n")


def test_something():
    assert True


def test_something2():
    assert True

```

上記のテスト関数を実行すると以下のようになる

```bash
pytest tests/test_startup_cleanup.py -sv

# ... 中略 ...

collected 2 items

tests/test_startup_cleanup.py::test_something
 --- setup function start ---

PASSED
 --- teardown function start ---


tests/test_startup_cleanup.py::test_something2
 --- setup function start ---

PASSED
 --- teardown function start ---

```

## テストクラスに対する前後処理

クラスの場合は、`setup_method()`, `teardown_method()` となる

テスト全体に対する前後処理は、`setup_class()`, `teardown_class()` というクラスメソッドで定義できる

```py
class TestStartupCleanupSampleClass:
    @classmethod
    def setup_class(cls):
        print("\n ~~~~~~~~~ setup class ~~~~~~~~~ \n")

    @classmethod
    def teardown_class(cls):
        print("\n ~~~~~~~~~ teardown class ~~~~~~~~~ \n")

    def setup_method(self, method):
        print("\n --- setup method --- \n")

    def teardown_method(self, method):
        print("\n --- teardown method --- \n")

    def test_something(self):
        assert True

    def test_something2(self):
        assert True
```

上記のテストを実行すると、以下のようになる

```bash
pytest tests/TestStartUpCleanupSampleClass.py -sv

# ... 中略 ...

tests/TestStartUpCleanupSampleClass.py::TestStartupCleanupSampleClass::test_something
 ~~~~~~~~~ setup class ~~~~~~~~~


 --- setup method ---

PASSED
 --- teardown method ---


tests/TestStartUpCleanupSampleClass.py::TestStartupCleanupSampleClass::test_something2
 --- setup method ---

PASSED
 --- teardown method ---


 ~~~~~~~~~ teardown class ~~~~~~~~~
```

## モジュールに対する前後処理

モジュール（スクリプト全体）の処理は、`setup_module` と `teardown_module` で定義できる

```py
def setup_module(function):
    print("\n ~~~~~~~~~~~~ setup_module ~~~~~~~~~~~~ \n")


def teardown_module(function):
    print("\n ~~~~~~~~~~~~ teardown_module ~~~~~~~~~~~~ \n")


def test_something():
    print("\n ---- test_something ---- \n")


class TestSampleClass:
    @classmethod
    def setup_class(cls):
        print("\n ---- setup_class ---- \n")

    @classmethod
    def teardown_class(cls):
        print("\n ---- teardown_class ---- \n")

    def test_something_class(method):
        print("\n ---- test_something_class ---- \n")
```

上記のテストを実行すると、以下のようになる

```bash
pytest tests/test_startup_cleanup_module.py -sv

# ... 中略 ...

tests/test_startup_cleanup_module.py::test_something
 ~~~~~~~~~~~~ setup_module ~~~~~~~~~~~~


 ---- test_something ----

PASSED
tests/test_startup_cleanup_module.py::TestSampleClass::test_something_class
 ---- setup_class ----


 ---- test_something_class ----

PASSED
 ---- teardown_class ----


 ~~~~~~~~~~~~ teardown_module ~~~~~~~~~~~~
```
