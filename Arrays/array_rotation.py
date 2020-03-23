import pytest

#ar: the array to be rotated
#d: the number of rotations
#n: the size of the array

#Output: the rotated array
#Time Complexity: O(n)
#Space Complexity: O(n)
def rotate_with_temp_array(ar, d, n):
    d = d%n
    temp = []
    for i in range(d, n):
        temp.append(ar[i])
    for i in range(0,d):
        temp.append(ar[i])
    return temp

