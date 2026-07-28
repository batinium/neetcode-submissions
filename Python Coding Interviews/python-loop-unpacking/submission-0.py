from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    best = 0
    name = ""
    for i , y in scores:
        if best < y:
            best = y
            name = i
    return name
             
        


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
