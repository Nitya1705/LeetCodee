class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
            
        is_negative = (dividend < 0) ^ (divisor < 0)
        
        dvd = abs(dividend)
        dvs = abs(divisor)
        
        quotient = 0
        
        while dvd >= dvs:
            temp_dvs = dvs
            multiple = 1
            
            while dvd >= (temp_dvs << 1):
                temp_dvs <<= 1
                multiple <<= 1
                
            dvd -= temp_dvs
            quotient += multiple
            
        if is_negative:
            quotient = -quotient
            
        return min(max(MIN_INT, quotient), MAX_INT)

        