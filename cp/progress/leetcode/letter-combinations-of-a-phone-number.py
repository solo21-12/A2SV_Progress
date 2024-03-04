class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_mapping = {
                '2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'
                }

        if not digits:
            return []

        def backtrack(i, comb):
            if i == len(digits):
                result.append("".join(comb))
                return

            for letter in phone_mapping[digits[i]]:
                comb.append(letter)
                backtrack(i + 1, comb)
                comb.pop()

        result = []
        backtrack(0,[])

        return result

            


        

            
