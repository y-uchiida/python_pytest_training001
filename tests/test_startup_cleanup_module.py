# モジュール（スクリプト全体）の前後処理
# setup_module() と teardown_module() で定義する


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
