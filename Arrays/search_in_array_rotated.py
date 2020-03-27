import math
#ar: the array to be rotated
#d: target
#n: the size of the array

#Output: index of target, -1 if not found

#TimeComplexity: O(logn)
#SpaceComplexity: O(1)
def binary_search_sorted_array(ar, d, n):
    minIndex = 0
    maxIndex = len(ar) - 1
    while minIndex <= maxIndex:
        middle = (maxIndex+minIndex)//2
        if(d == ar[middle]):
            return middle
        elif(d < ar[middle]):
            maxIndex = middle - 1
        elif(d > ar[middle]):
            minIndex = middle + 1
    return -1

#TimeComplexity: O(logn)
#SpaceComplexity: O(logn)
def binary_search_sorted_array_recursive(ar, minI, maxI, d, n):
    if(minI > maxI):
        return -1
    middle = (minI+maxI)//2
    if(d == ar[middle]):
        return middle
    elif(d < ar[middle]):
        return binary_search_sorted_array_recursive(ar, minI, middle - 1, d, n)
    else:
        return binary_search_sorted_array_recursive(ar, middle + 1, maxI, d, n)


def binary_search_rotated_array_recursive(ar, minI, maxI, d):    
    if (minI > maxI): 
        return -1
      
    middle = (minI+maxI)//2
    if (ar[middle] == d): 
        return middle
    if ar[minI] <= ar[middle]: 
        if d >= ar[minI] and d <= ar[middle]: 
            return binary_search_rotated_array_recursive(ar, minI, middle-1, d) 
        return binary_search_rotated_array_recursive(ar, middle+1, maxI, d) 

    if d >= ar[middle] and d <= ar[maxI]: 
        return binary_search_rotated_array_recursive(a, middle+1, maxI, d) 
    return binary_search_rotated_array_recursive(ar, minI, middle-1, d)