class Solution:
    def decodeString(self, s: str) -> str:

        def decode(s):
            ans = str()
            prev = 0
            repetitions = 0
            depth = 0  # keeps track of # open bracket - # close bracket
            for i in range(len(s)):
                if depth == 0 and "a" <= s[i] <= "z":
                    # case with lowercase letters
                    ans += s[i]
                    prev = i + 1
                if s[i] == "[":
                    depth += 1
                    if depth == 1:  # open bracket for the case "k[s]"
                        repetitions = int(s[prev:i])
                        prev = i + 1
                elif s[i] == "]":
                    depth -= 1
                    if depth == 0:  # close bracket for the case "k[s]"
                        while repetitions > 0:  # add k copies of s
                            ans += decode(s[prev:i])
                            repetitions -= 1
                        prev = i + 1
            return ans



        return decode(s)
