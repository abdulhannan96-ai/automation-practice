import pytest
@pytest.yield_fixture()
def setup():
    print("Opening URL to Login")
    yield
    print("Closing Browser after Login")

def test_loginbyemail(setup):
    print("logging in by email")
    print("Done LogIn")

def test_loginbyfacebok(setup):
    print("Logging in by Facebook")
    print("Done LogIn")
