"""
These exercises focus on different approaches for writing property-based tests.

Try to find more than one test case for each exercise and test the functions under test extensively.
"""
import pytest
from hypothesis import given, strategies as st

# Exercise 1: Use Hypothesis to test the `reversed` built-in function for lists

# Your strategy goes here
@given(st.lists(st.text()))
def test_reversed(input_list):
  # Your test goes here
  #assert list(string) == list(reversed(list(reversed(list(string)))))
  assert input_list == list(reversed(list(reversed(input_list))))

# Additional test cases go here



# Exercise 2: Use Hypothesis to test the `sorted` built-in function for lists.

# Your strategy goes here
@given(st.lists(st.text()))
def test_sorted(input_list):
  # Your test goes here
  assert sorted(input_list, reverse=True) == list(reversed(sorted(input_list)))

# Additional test cases go here



# Exercise 3: Use Hypothesis to test the `enumerated` built-in function for lists.

# Your strategy goes here
@given(st.lists(st.text(min_size=1), min_size=1))
def test_enumerated(input_list):
  # Your test goes here
  assert (0, input_list[0]) == next(enumerate(input_list))
