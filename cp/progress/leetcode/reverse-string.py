class Solution:
    def reverse(self, s, l):
        N = len(s)
        if l >= N // 2:
            return

        s[l], s[N - l -1]=  s[N - l -1], s[l]
        return self.reverse(s, l + 1)

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0)