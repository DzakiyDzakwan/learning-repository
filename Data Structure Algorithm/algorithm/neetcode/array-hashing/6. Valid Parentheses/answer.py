class Solution(object):
    def isValid(self, s):
        stack = []

        bracket = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for char in s:
            if char in bracket.values():
                stack.append(str(char))
            elif char in bracket.keys():
                if not stack or bracket[char] != stack.pop():
                    return False

        return not stack
        