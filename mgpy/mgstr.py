"""A personal module containing methods I use once in a while."""
from enum import StrEnum

class Loglevel(StrEnum):
    """A string enum defining importance levels for usage in the 'log_print' method"""
    INFO = 'Information'
    WARNING = 'Warning'
    ERROR = 'ERROR'

def log_print(s: str, level: Loglevel = Loglevel.INFO):
    """Takes a string and outputs it with an additional prefix indicating importance."""
    print(f'{level}: {s}')

def truncate_string(s: str, length: int, ellipsis: str = '...') -> str:
    """Takes a string, truncates it to {length - n} (where n is the lenght of the ellipsis) characters and adds an ellipsis (default is '...').
    If the argument {s} is not a string, the method just returns the argument.
    """
    if not isinstance(length, int):
        length = len(s)
    if not isinstance(ellipsis, str):
        ellipsis = '...'
    if not isinstance(s, str):
        print(f'{s} is not a string.')
    elif len(s) > length:
        # if the shortened string including the ellipsis is too long, don't add an ellipsis
        if len(ellipsis) > length - len(ellipsis):
            ellipsis = ''
        s = f'{s[:length-len(ellipsis)]}{ellipsis}'
    return s
