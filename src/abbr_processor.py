"""
Find abbrevations definition in text.
"""


def find_words(abbr: str, text: str) -> str:
    """
    >>> find_words('OT', 'This is Off Topic')
    'Off Topic'
    """
    n_chars = len(abbr)
    return ' '.join(text.split()[-n_chars:])
