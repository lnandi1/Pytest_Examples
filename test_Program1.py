import inspect

def the_function(x, y):
    return x*y


def test_math():
    x = 2
    y = 3
    expected = 6
    assert the_function(x, y) == expected

def test_source():
    source_code = inspect.getsource(the_function)
    assert 'range(' in source_code
