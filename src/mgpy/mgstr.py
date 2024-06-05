"""A personal module containing methods I use once in a while."""
from enum import StrEnum

class Loglevel(StrEnum):
    """A string enum defining importance levels for usage in the 'log_print' method"""
    INFO = 'Information'
    WARNING = 'Warning'
    ERROR = 'ERROR'

def log_print(s, level=Loglevel.INFO):
    """Takes a string and outputs it with an additional prefix indicating importance."""
    print(f'{level}: {s}')

def truncate_string(s, length, ellipsis='...'):
    """Takes a string, truncates it to {length-3} characters and adds '...'.
    If the argument {s} is not a string, the method just returns the argument.
    """
    if not isinstance(ellipsis, str):
        ellipsis = '...'
    if not isinstance(s, str):
        print(f'{s} is not a string.')
    elif len(s) > length:
        s = f'{s[:length-len(ellipsis)]}{ellipsis}'
    return s
