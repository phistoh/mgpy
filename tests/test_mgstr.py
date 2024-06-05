import io
import sys

from mgpy import mgstr

def test_log_print():
    hello_world = "Hello, world!"

    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    mgstr.log_print(hello_world)
    sys.stdout = sys.__stdout__

    assert f"Information: {hello_world}\n" == capturedOutput.getvalue()


def test_log_print_with_loglevel_error():
    hello_world = "Hello, world!"

    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    mgstr.log_print(hello_world, mgstr.Loglevel.ERROR)
    sys.stdout = sys.__stdout__

    assert f"ERROR: {hello_world}\n" == capturedOutput.getvalue()


def test_log_print_with_invalid_loglevel():
    hello_world = "Hello, world!"

    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    mgstr.log_print(hello_world, [])
    sys.stdout = sys.__stdout__

    assert f"Information: {hello_world}\n" == capturedOutput.getvalue()


def test_truncate_string():
    long_string = "long string is very long"

    truncated_string = mgstr.truncate_string(long_string, 11 + 3)

    assert "long string..." == truncated_string


def test_truncate_string_with_ellipsis():
    long_string = "long string is very long"

    truncated_string = mgstr.truncate_string(long_string, 11 + 1, "…")

    assert "long string…" == truncated_string


def test_truncate_string_with_too_short_length():
    short_string = "short string"

    truncated_string = mgstr.truncate_string(short_string, 2)

    assert "sh" == truncated_string
