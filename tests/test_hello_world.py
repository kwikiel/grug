# Write hello world test using pytest
#
from grug_coder.main import hello_world
# Path: tests/test_hello_world.py

def test_hello_world():
    assert hello_world() == "Hello, World!"