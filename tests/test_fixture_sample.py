# fixture を利用すると、柔軟な前後処理の設定ができる
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
