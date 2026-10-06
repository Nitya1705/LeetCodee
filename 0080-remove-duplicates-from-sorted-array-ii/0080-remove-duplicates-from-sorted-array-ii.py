class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        # Start placing valid elements from index 2
        start = 2 
        
        for i in range(2, n):
            # Compare current element with the element two positions behind the write pointer
            if nums[i] != nums[start - 2]:
                nums[start] = nums[i]
                start += 1
                
        return start
