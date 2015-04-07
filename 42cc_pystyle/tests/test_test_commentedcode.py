import StringIO
import sys
import tokenize

sys.path.append('..')

import test_comments

T = test_comments.commentedcode


def test_ok_function():
    'non-commented code'
    code = 'def func(): pass'
    tokens = tokenize.generate_tokens(StringIO.StringIO(code).readline)
    assert T(code, tokens) is None


def test_commentedcode():
    'code contains commented out parts, we should catch 2nd line'
    code = '''def f():
    #if True:
    #    pass
    if False:
        pass
    x = 1
'''
    tokens = tokenize.generate_tokens(StringIO.StringIO(code).readline)
    msg = T(code, tokens)
    assert msg == (4, '42cc4: Commented out code'), msg


def test_code_with_comments():
    'code contains end-of-line comments'
    code = '''def f():  # lets do it
    def nested():  # shortcut
      pass
'''
    tokens = tokenize.generate_tokens(StringIO.StringIO(code).readline)
    msg = T(code, tokens)
    assert msg is None, msg
