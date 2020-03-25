import search_in_array_rotated
import pytest

def test_binary_search_sorted_array():
    ar = [0,1,2,3,4,5,6,7]
    output = 3
    assert search_in_array_rotated.binary_search_sorted_array(ar, output, 8) == output

def test_binary_search_sorted_array_recursive():
    ar = [0,1,2,3,4,5,6,7]
    output = 3
    assert search_in_array_rotated.binary_search_sorted_array_recursive(ar, 0, 7, output, 8) == output
