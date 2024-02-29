class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        peoples = [[name, height] for name, height in zip(names, heights)]
        peoples.sort(key = lambda x:x[1], reverse=True)

        ans = [person[0] for person in peoples]

        return ans
        