from python_starting_project.core import greet


def test_greet_returns_expected_message():
    assert greet("Tester") == "Hello, Tester!"
