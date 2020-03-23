import array_rotation
import pytest

def test_rotate_with_temp_array():
    ar = [1,2,3,4,5,6]
    output = [3,4,5,6,1,2]
    assert array_rotation.rotate_with_temp_array(ar, 2, 6) == output
    assert array_rotation.rotate_with_temp_array(ar, 8, 6) == output

def test_rotate_inplace_with_recursion():
    ar = [1,2,3,4,5,6]
    output = [4,5,6,1,2,3]
    assert array_rotation.rotate_inplace_with_recursion(ar, 3, 6) == output

    #Reninitalize because of inplace rotation
    ar1 = [1,2,3,4,5,6]
    assert array_rotation.rotate_inplace_with_recursion(ar1, 9, 6) == output