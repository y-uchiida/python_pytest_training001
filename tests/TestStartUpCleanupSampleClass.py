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
