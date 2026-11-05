class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "]" : "[",
            ")" : "(",
            "}" : "{"
        }
        
        stack = []

        for c in s:
            # left bucket
            if c not in pairs:
                stack.append(c)
            else:
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0        