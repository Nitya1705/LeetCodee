class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        prod = 1
        sum_1 = 0
        diff = 0
        while temp > 0:
            r = temp%10
            temp//=10
            sum_1+=r
            prod*=r
        diff = prod - sum_1
        return diff
        