class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        data_gen = {"(": ")", "{": "}", "[": "]"}
        for ch in s:
            if data_gen.get(ch):
                stack.append(ch)
            elif data_gen[stack[-1]] == ch:
                stack.pop()
            else:
                return False
        return len(stack) == 0


is_ins = Solution()
print(is_ins.isValid("()"))
print(is_ins.isValid("()[]{}"))
print(is_ins.isValid("(]"))
print(is_ins.isValid("([])"))
print(is_ins.isValid("([)]"))