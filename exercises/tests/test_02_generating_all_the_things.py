"""
This part of the workshop focuses on specifying which data we want Hypothesis to generate.

The Hypothesis documentation on available strategies will be helpful for this:
https://hypothesis.readthedocs.io/en/latest/data.html

Remember: You can explore the values generated by strategies by calling their .example() method in a Python shell.
"""

from dataclasses import dataclass
from typing import Optional

import pytest
from hypothesis import given, strategies as st

# Exercise 1: Write a strategy the generates even integers

# Your code goes here
#@pytest.mark.skip  # Remove this
@given(st.integers().filter(lambda x: x % 2 == 0))
def test_even_integers(i):
    assert i % 2 == 0



# Exercise 2: Write a strategy that generates 2-tuples of integers

# Your code goes here
@given(
    st.tuples(st.integers(), st.integers())
)
def test_tuples(t):
    assert len(t) == 2
    assert isinstance(t[0], int)
    assert isinstance(t[1], int)



# Exercise 3: Write a strategy that generates 2-tuples of integers, where the second integer is larger than the first

# Your code goes here
@given(
    st.tuples(st.integers(), st.integers()).map(sorted).filter(lambda x: x[0] < x[1])
)
def test_tuples_with_larger_second_value(t):
    assert len(t) == 2
    assert t[0] < t[1]



# Exercise 4: Given a dataclass "Container" that stores an integer "id", and a string "value". Write a strategy that generates examples for that dataclass.
@dataclass
class Container():
    id: int
    value: str


# Your code goes here
@given(
    st.builds(
        Container,
        id=st.integers(min_value=1),
        value=st.text()
    )
)
def test_container(container):
    assert isinstance(container, Container)
    assert isinstance(container.id, int)
    assert isinstance(container.value, str)



# Exercise 5: If we want to write more tests for the Container type, we will have to copy and paste the strategy all over the place. The goal of this example is to make the strategy reusable for different tests. Write a composite strategy that returns Container objects. The composite strategy should have optional keyword arguments that allows users to override the strategies used to generate Container.id and Container.value. If no strategies for Container.id or Container.value are given, fall back to the defaults.

@st.composite
def containers(draw, id=st.integers(min_value=1), value=st.text()) -> Container:
    # Your code goes here
    return draw(st.builds(Container, id=id, value=value))


@given(
    containers(id=st.integers(min_value=1))
)
def test_container_with_positive(container):
    assert isinstance(container, Container)
    assert container.id > 0
    assert isinstance(container.value, str)



# Bonus exercise 1: Write a Point3D dataclass with three floating point attributes x, y, and z. Write a reusable Hypothesis strategy for Point3D.

# Bonus exercise 2: Look at the documentation of the "deferred" strategy (see https://hypothesis.readthedocs.io/en/latest/data.html#hypothesis.strategies.deferred). Write a Hypothesis strategy that generates the following "Node" data structure.

@dataclass
class Node:
    value: int
    left: Optional["Node"]
    right: Optional["Node"]
