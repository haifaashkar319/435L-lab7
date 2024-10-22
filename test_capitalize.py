# test_capitalize.py
import pytest
from capitalize import capital_case

# Test to check proper capitalization
def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

# Test to check exception handling for non-string input
def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)
