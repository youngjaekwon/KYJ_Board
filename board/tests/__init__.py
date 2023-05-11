import unittest


def sute():
    return unittest.TestLoader().discover("board.tests", pattern="test_*.py")
