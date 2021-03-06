import ast
import sys

sys.path.append('..')

import test_single_if

T = test_single_if.TestSingleIf


def test_ok_function():
    'simple function should be ok'
    assert list(T(ast.parse('def func(): pass')).run()) == []


def test_singleif_function():
    'function with a single `if` should fail'
    f = '''def f():
    if True:
        pass
'''
    msg = list(T(ast.parse(f)).run())
    assert msg == [
        (1, 0, '42cc3: Function should be longer than a single if',
         '42cc3')], msg


def test_twoif_function():
    'function longer than a single if, should be ok'
    f = '''def f():
    if True:
        pass
    if False:
        pass
'''
    msg = list(T(ast.parse(f)).run())
    assert msg == []
