class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        changes = defaultdict(int)
        PRICE = 5

        for bill in bills:
            if bill > PRICE:
                if bill == 10:
                    if not changes[PRICE]:
                        return False

                    changes[bill] += 1
                    changes[PRICE] -= 1
                else:
                    if changes[10] and changes[PRICE]:
                        changes[10] -= 1
                        changes[PRICE] -= 1
                    elif changes[5] >= 3:
                        changes[PRICE] -= 3
                    else:
                        return False

                    changes[bill] += 1         
            else:
                changes[bill] += 1

        return True
           
        