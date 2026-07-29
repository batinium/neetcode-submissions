from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    arr2 = []
    # Loop once for each item in the list
    for _ in range(len(arr)):
        arr2.append(arr.pop())
    return arr2

# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
