class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                
                while stack and stack[-1] * asteroid < 0 and abs(asteroid) > stack[-1]:
                    stack.pop()

                if stack:
                    if stack[-1] < 0:
                        stack.append(asteroid)
                    elif stack[-1] == abs(asteroid):
                        stack.pop()
                else:
                    stack.append(asteroid)

        return stack
        