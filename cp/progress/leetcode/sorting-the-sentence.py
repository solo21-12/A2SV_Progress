class Solution:
    def sortSentence(self, s: str) -> str:
        ch = list(s.split(" "))
        ch.sort(key=lambda x: x[-1])

        for i in range(len(ch)):
            ch[i] = ch[i][:-1]

        return " ".join(ch)
