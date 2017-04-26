import pytest

from src.pkgexemple.welcome import *

def test_int_randomizer_return42():
    assert int_randomizer() == 42

def test_say_something_string():
    toTest = say_something("Test string")
    assert toTest =="Hello World, I must tell you something: Test string."
