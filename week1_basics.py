"""
Week 1: Python Fundamentals
Your task: implement each function so that it passes the tests in tests/test_week1_basics.py
"""

def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    # TODO: implement
    return a+b


def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome, ignoring spaces and case."""
    # TODO: implement
    s = s.replace(" ", "").lower()
    return s == s[::-1]


def flatten_list(nested: list) -> list:
    """Flatten a list of lists into a single list."""
    # TODO: implement
    result = []
    for sublist in nested:
        result.extend(sublist)
    return result
    


def count_words(sentence: str) -> dict:
    """Return a dict with word counts (case-insensitive)."""
    # TODO: implement
    words = sentence.lower().split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


def find_max(numbers: list) -> int:
    """Return the maximum number in the list. Assume list is non-empty."""
    # TODO: implement
    return max(numbers)
