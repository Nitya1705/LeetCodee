class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result =[]
        r_sum =0

        for i in range(n):
            r_sum = r_sum + nums[i]
            result.append(r_sum)
        return result