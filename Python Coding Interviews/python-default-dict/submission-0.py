from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    dic = defaultdict(int)

    for c in s:
        dic[c] +=1

    return dic


def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    dic = defaultdict(list)

    for sublist in nums:
        # Extend the list at key sublist[0] with the rest of the elements sublist[1:]
        dic[sublist[0]].extend(sublist[1:])

    return dic


# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
