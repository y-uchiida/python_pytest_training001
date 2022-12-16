# 06 mark の利用

mark を利用することで、テスト関数やクラスにグループを設定できる

```py
import pytest

@pytest.mark.fooGroup
```

## 設定ファイルへの記述

`@pytest.mark` で利用する名称は、設定ファイルにあらかじめ記載しておく必要がある  
`pyproject.toml` に対応しているので、poetry プロジェクトの場合は以下のように書ける

```toml
[tool.pytest.ini_options]
markers = [
	"fooGroup",
	"barGroup",
]
```

`pytest.ini` に設定する場合は以下

```ini
[pytest]
markers =
	"fooGroup",
	"fooClassGroup",
	"barGroup",
	"barClassGroup",
```

## mark の利用例

```py
import pytest


@pytest.mark.fooGroup
def test_sample_foo1():
    assert True


@pytest.mark.fooGroup
def test_sample_foo2():
    assert True


@pytest.mark.fooGroup
def test_sample_foo3():
    assert True


@pytest.mark.fooGroup
class TestFooClassSample:
    @pytest.mark.fooClassGroup
    def test_fooclass(self):
        assert True


@pytest.mark.barGroup
def test_sample_bar1():
    assert True


@pytest.mark.barGroup
def test_sample_bar2():
    assert True


@pytest.mark.barGroup
def test_sample_bar3():
    assert True


@pytest.mark.barGroup
class TestBarClassSample:
    @pytest.mark.barClassGroup
    def test_barclass(self):
        assert True
```

`pytest -m グループ名` で指定してテストを実行すると、そのグループに属するテストだけが処理される

```bash
# fooGroup を指定する場合
pytest -m fooGroup -v

# ... 中略 ...

rootdir: /home/y-uchiida/develop/python_trainings/python_pytest_training001, configfile: pyproject.toml
collected 8 items / 4 deselected / 4 selected

tests/test_mark_sample.py::test_sample_foo1 PASSED                                                     [ 25%]
tests/test_mark_sample.py::test_sample_foo2 PASSED                                                     [ 50%]
tests/test_mark_sample.py::test_sample_foo3 PASSED                                                     [ 75%]
tests/test_mark_sample.py::TestFooClassSample::test_fooclass PASSED                                    [100%]

# barGroup を指定する場合
pytest -m barGroup -v

# ... 中略 ...

rootdir: /home/y-uchiida/develop/python_trainings/python_pytest_training001, configfile: pyproject.toml
collected 8 items / 4 deselected / 4 selected

tests/test_mark_sample.py::test_sample_bar1 PASSED                                                     [ 25%]
tests/test_mark_sample.py::test_sample_bar2 PASSED                                                     [ 50%]
tests/test_mark_sample.py::test_sample_bar3 PASSED                                                     [ 75%]
tests/test_mark_sample.py::TestBarClassSample::test_barclass PASSED                                    [100%]

```

## mark.skip

`@pytest.mark.skip` デコレータをつけると、テストをスキップすることができる

```py
import pytest


def test_something():
    assert True

# reason に、スキップの理由を記載できる
@pytest.mark.skip(reason="not implemented")
def test_skipped():
    assert True
```

上記のテストを実行すると、以下のようになる

```bash
pytest -v

rootdir: /home/y-uchiida/develop/python_trainings/python_pytest_training001, configfile: pyproject.toml
collected 2 items

tests/test_mark_skip.py::test_something PASSED                                                   [ 50%]
tests/test_mark_skip.py::test_skipped SKIPPED (not implemented)                                  [100%]

==================================== 1 passed, 1 skipped in 0.01s ====================================

```

## pytest の -m オプション

mark を指定するオプション  
"not <グループ名>" と指定することで、指定のグループ以外を実行することもできる
