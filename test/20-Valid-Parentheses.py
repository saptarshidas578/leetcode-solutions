class Solution:
    def isValid(self, s: str) -> bool:
        d = {")": "(", "]": "[", "}": "{"}
        stack = []
        for i in s:
            if i in "[{(":
                stack.append(i)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != d[i]:
                    return False
        return len(stack) == 0
