def the_function(x, y):
    return x*y


def test_beep():
    x = 1
    y = 3
    expected = 6
    assert the_function(x, y) == expected
