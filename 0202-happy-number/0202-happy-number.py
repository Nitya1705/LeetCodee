class Solution:
    def isHappy(self, n: int) -> bool:
         sett = set()

         while n!=1:
            str_num = str(n)
            n = sum(int(d)**2 for d in str_num)
            
            if n !=1 and n in sett:
                return False
            else:
                sett.add(n)
         return True