class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        l,r = 1, len(skill) - 2
        minSum = skill[0] + skill[-1]
        # print(minSum)

        ans = skill[0] * skill[-1]
        while l < r:
            print()
            if skill[l] + skill[r] != minSum:
                return -1
            
            ans += (skill[l] * skill[r])
            l += 1
            r -= 1

        return ans
        