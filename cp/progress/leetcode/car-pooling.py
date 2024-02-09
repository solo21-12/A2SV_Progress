class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        carPools = {}

        for numPassengers,start,end in trips:
            carPools[start] = carPools.get(start,0) + numPassengers
            carPools[end] = carPools.get(end,0) - numPassengers

        newPool = sorted(carPools.items(), key= lambda x:x[0])

        currCapacity = 0
        for key,amount in newPool:
            currCapacity += amount

            if currCapacity > capacity:
                return False

        return True

        