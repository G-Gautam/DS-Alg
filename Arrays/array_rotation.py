#ar: the array to be rotated
#d: the number of rotations
#n: the size of the array

#Output: the rotated array

#Time Complexity: O(n)
#Space Complexity: O(n)
def rotate_with_temp_array(ar, d, n):
    d = d%n
    temp = []
    if(len(ar) == 0):
        return temp
    for i in range(d, n):
        temp.append(ar[i])
    for i in range(0,d):
        temp.append(ar[i])
    return temp

#Time Complexity: O(n)
#Space Complexity: O(n)
def rotate_inplace_with_recursion(ar, d, n):
    if(len(ar) == 0):
        return ar;
    if(d == 0):
        return ar
    x = ar.pop(0)
    ar.append(x)
    return rotate_inplace_with_recursion(ar, d-1, n)

#Time Complexity: O(n)
#Space Complexity: O(1)
def rotate_inplace_dynamic_list(ar, d, n):
    if(len(ar) == 0):
        return ar;
    d = d%n
    for i in range(d):
        ar.insert(len(ar), ar.pop(0))
    return ar
    