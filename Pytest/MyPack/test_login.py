import pytest


@pytest.yield_fixture()
def setup():
    print("Opening URL to SignUp")
    yield
    print("Closing Browser after SignUp")


def test_signupbyemail(setup):
    print("SignUp by email")
    print("Done SignUp")


def test_signupbyfacebok(setup):
    print("SignUp by Facebook")
    print("Done SignUp")
