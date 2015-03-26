import ast
import sys

sys.path.append('..')

import test_len_function

T = test_len_function.TestLenFunction


def test_short_function():
    'short function should pass'
    assert list(T(ast.parse('def func(): pass')).run()) == []


def test_long_function():
    'Very long function should fail'
    f = '\n'.join(['def f():'] + ['    x = 1']*50)
    msg = list(T(ast.parse(f)).run())
    assert msg == [
        (1, 0, '42cc2: Function should be shorter than 40 statements',
         '42cc2')], msg
