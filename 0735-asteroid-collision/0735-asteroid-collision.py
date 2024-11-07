class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        asteroidStack = [asteroids[0]]
        i = 1
        while i < len(asteroids):
            if (asteroidStack and asteroids[i] < 0 and asteroidStack[-1] > 0):
                if abs(asteroids[i]) == abs(asteroidStack[-1]):
                    asteroidStack.pop()     
                    i += 1
                elif asteroids[i] < 0 and asteroidStack[-1] > 0 and abs(asteroids[i]) > abs(asteroidStack[-1]):
                    while asteroidStack and asteroids[i] < 0 and asteroidStack[-1] > 0 and abs(asteroids[i]) > abs(asteroidStack[-1]):
                        asteroidStack.pop()
                else:
                    i += 1
            else:
                asteroidStack.append(asteroids[i])
                i += 1
        return asteroidStack
                
                
                