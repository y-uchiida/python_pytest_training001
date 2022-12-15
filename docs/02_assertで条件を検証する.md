# 02_assert で条件を検証する

`assert` で条件文の検証を行うことができる  
`True` の 場合は Pass し、 `False` の場合は Fail になる

```py
def test_assertの実行_Trueの場合():
    # assert は、結果が True の場合にテストをPassさせる
    assert 1 == 1


def test_assertの実行_Falseの場合():
    # 結果が False になるテストはFail になる
    assert (1 + 1) == 3
```

```bash
# -v オプションで、実行したテストの名称と結果を列挙する
pytest -v

#... 中略 ...

tests/test_sample.py::test_hello_world PASSED                                                  [ 33%]
tests/test_sample.py::test_assertの実行_Trueの場合 PASSED                                       [ 66%]
tests/test_sample.py::test_assertの実行_Falseの場合 FAILED                                      [100%]
```
