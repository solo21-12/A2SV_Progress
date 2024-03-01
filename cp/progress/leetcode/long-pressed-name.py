class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l, r = 0, 0

        while l < len(name) and r < len(typed):
            if name[l] == typed[r]:
                l += 1
                r += 1
            elif l == 0:
                return False
            else:
                while r < len(typed) and typed[r] != name[l] and typed[r] == name[l-1]:
                    r += 1

                if r < len(typed) and typed[r] != name[l-1] and typed[r] != name[l]:
                    return False

        while r < len(typed):
            if typed[r] != name[-1]:
                return False
            r += 1

        return l == len(name)
        