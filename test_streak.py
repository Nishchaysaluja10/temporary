import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    """Test that the function returns the longest of multiple streaks."""
    assert longest_positive_streak([1, 2, -3, 4, 5, 6, -7, 8]) == 3

def test_with_zeros():
    """Test that zeros reset the streak count."""
    assert longest_positive_streak([1, 2, 0, 3, 4]) == 2

def test_with_negatives():
    """Test that negative numbers reset the streak count."""
    assert longest_positive_streak([-1, -2, 1, 2, 3, -4, 5]) == 3

def test_no_positive_numbers():
    """Test a list with no positive numbers returns 0."""
    assert longest_positive_streak([-1, -2, -3, 0]) == 0

def test_all_positive_numbers():
    """Test a list with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_element_list():
    """Test a single element list."""
    assert longest_positive_streak([1]) == 1
    assert longest_positive_streak([-1]) == 0

def test_streak_at_end():
    """Test when the longest streak is at the end of the list."""
    assert longest_positive_streak([1, -2, 3, 4, 5]) == 3