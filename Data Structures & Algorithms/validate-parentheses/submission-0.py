class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs={
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for c in s:
            if c in pairs.values():
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    top = stack.pop()
                    if top != pairs[c]:
                        return False
        
        return len(stack) == 0



        