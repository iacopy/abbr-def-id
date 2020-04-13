"""
Test the identification of abbreviated words.
"""
# 3rd party
import pytest

# My stuff
from abbr_processor import find_words


@pytest.mark.parametrize('abbr,text,expected', [
    ['OT', 'This is Off Topic', 'Off Topic'],
    ['AR', 'case-control study to assess if androgen receptor ', 'androgen receptor'],
])
def test_find_words_basic(abbr, text, expected):
    """Simple abbrevation cases"""
    assert find_words(abbr, text) == expected


@pytest.mark.xfail(descr='not implemented')
@pytest.mark.parametrize('abbr,text,expected', [
    ['AGA', 'used against male androgenetic alopecia ', 'androgenetic alopecia'],
])
def test_find_words_complex(abbr, text, expected):
    """Complex abbrevation cases"""
    assert find_words(abbr, text) == expected
