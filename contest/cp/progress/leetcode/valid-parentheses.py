class Solution:
    def isValid(self, s: str) -> bool:
        opens = { "{":"}", "(":")", "[":"]" }
        stack = []

        for ch in s:
            if ch in opens:
                stack.append(ch)
            elif not stack:
                return False
            else:
                top = stack.pop()

                if opens[top] != ch:
                    return False

        return True if not stack else False
