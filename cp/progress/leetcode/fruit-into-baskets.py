class Solution:
    def totalFruit(self,fruits):
        max_sum = 0
        curr_sum = 0
        curr_fruits = defaultdict(int)

        l,r = 0,0

        for r in range(len(fruits)):
            curr_fruits[fruits[r]] += 1
            curr_sum += 1

            while len(curr_fruits) >  2:
                curr_fruits[fruits[l]] -= 1
                curr_sum -= 1

                if curr_fruits[fruits[l]] == 0:
                    curr_fruits.pop(fruits[l])

                l += 1
                    
            max_sum = max(max_sum, curr_sum)


        return max_sum  



        