class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif not stack or stack.pop() != bracket_map[c]:
                return False
        return True if not stack else False

        