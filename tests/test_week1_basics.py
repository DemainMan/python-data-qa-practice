import pytest
from week1_basics import add, is_palindrome, flatten_list, count_words, find_max


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("hello") is False


def test_flatten_list():
    assert flatten_list([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten_list([[1], [2, [3]]]) == [1, 2, [3]]  # only one level


def test_count_words():
    result = count_words("Hello hello world")
    assert result == {"hello": 2, "world": 1}


def test_find_max():
    assert find_max([3, 1, 4, 2]) == 4
    assert find_max([-5, -2, -9]) == -2
    assert find_max([7]) == 7
