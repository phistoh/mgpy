"""A personal module containing methods I use once in a while."""

from enum import StrEnum


class Loglevel(StrEnum):
    """A string enum defining importance levels for usage in the 'log_print' method"""

    INFO = "Information"
    WARNING = "Warning"
    ERROR = "ERROR"


def log_print(s: str, level: Loglevel = Loglevel.INFO):
    """Takes a string and outputs it with an additional prefix indicating importance."""
    if level not in Loglevel._member_names_:
        level = Loglevel.INFO
    print(f"{level}: {s}")


def truncate_string(s: str, length: int, ellipsis: str = "...") -> str:
    """Takes a string, truncates it to {length - n} (where n is the lenght of the ellipsis) characters and adds an ellipsis (default is '...').
    If the argument {s} is not a string, the method just returns the argument.
    """
    if not isinstance(length, int):
        length = len(s)
    if not isinstance(ellipsis, str):
        ellipsis = "..."
    if not isinstance(s, str):
        print(f"{s} is not a string.")
    elif len(s) > length:
        # if the shortened string including the ellipsis is too long, don't add an ellipsis
        if len(ellipsis) > length - len(ellipsis):
            ellipsis = ""
        s = f"{s[:length-len(ellipsis)]}{ellipsis}"
    return s


def insert_line_into_string(l, s, pos):
    """Takes two strings and inserts the first one `l` into the second one `s` as a new line at position `pos`"""
    split_string = s.splitlines(keepends=True)
    if "\n" not in l:
        l += "\n"
    if pos >= len(split_string):
        l = "\n" + l
        if "\n" not in split_string[-1]:
            l = l.rstrip("\n")
    split_string.insert(pos, l)
    return "".join(split_string)
