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
