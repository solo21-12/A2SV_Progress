class Solution:
    def smallestNumber(self, num: int) -> int:

        if len(str(num)) == 1:
            return num
        if num < 0:
            num = -num
            num = list(str(num))
            num.sort(reverse = True)
            return int("".join(num)) * -1
        else:
            num = list(str(num))
            num.sort()
            if num[0] == "0":
                i = 0
                while i < len(num) and num[i] == '0':
                    i+= 1
                    
                num[0], num[i] = num[i], num[0]

            res = int("".join(num))

            return res if res else 0


        