from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    left = 0
    right = len(arr) -1 

    while left < right:
        arr[left], arr[right] = arr[right],arr[left]
        left +=1
        right -=1
    return arr

# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
