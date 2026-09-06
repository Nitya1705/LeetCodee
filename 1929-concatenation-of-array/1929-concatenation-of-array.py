class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for n in nums:
            ans.append(n)
            ans = nums+nums
        return ans

        