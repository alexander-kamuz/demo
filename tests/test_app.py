from demo.app import greet


def test_greet():
    assert greet("Compass") == "Hello, Compass!"
