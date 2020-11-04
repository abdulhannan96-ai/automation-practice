import  pytest
@pytest.yield_fixture()
def setup():
    print("Once before every method")
    yield
    print("once after every method")

def testMethod1(setup):
    print("Test method 1.....")

def testMethod2(setup):
    print("Test method 2....")
