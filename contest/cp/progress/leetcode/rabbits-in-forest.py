class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits = defaultdict(int)
        res = 0

        for answer in answers:
            if not rabbits[answer]:
                res += answer  + 1
                
            rabbits[answer] += 1


            if rabbits[answer] == answer + 1:
                rabbits.pop(answer)


        return res
        