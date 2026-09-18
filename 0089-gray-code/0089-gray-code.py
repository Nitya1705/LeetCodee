class Solution:
    def grayCode(self, n: int) -> list[int]:
        result = [0]
        
        for i in range(n):
            # Reflect the current sequence 
            result += [x | (1 << i) for x in reversed(result)]
            
        return result
        