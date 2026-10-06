class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        start = 0
        for i in range(1 , n):
            #unique element
            if nums[i]!=nums[start]:
                  start+=1
                  nums[start]=nums[i]
                  # array will be rearranged
        return start+1  
        