class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # recusrion method
        # base case
        if n<=0:
            return False
        if n==1:
            return True
        if n%2!=0:
            return False
        # recursive case
        return self.isPowerOfTwo(n//2)


        # while n%2==0:
        #     n//=2

        # if n==1:
        #     return True
        # else:
        #     return False

        