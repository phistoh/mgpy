from mgpy import mgstr

def test_truncate_string():
    assert 'long string...' == mgstr.truncate_string('long string is very long', 11 + 3)

def test_truncate_string_with_ellipsis():
    assert 'long string…' == mgstr.truncate_string('long string is very long', 11 + 1, '…')

def test_truncate_string_with_too_short_length():
    assert 'sh' == mgstr.truncate_string('short string', 2)
