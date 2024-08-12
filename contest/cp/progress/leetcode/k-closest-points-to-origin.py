class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sorted_points = sorted(points,key = lambda x:math.sqrt(x[0]**2 + x[1]**2))

        return sorted_points[:k]
        