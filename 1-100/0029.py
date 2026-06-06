class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Step 1: Determine sign (True if signs are different)
        negative = (dividend < 0) != (divisor < 0)
        
        # Step 2: Work with absolute values
        a, b = abs(dividend), abs(divisor)
        result = 0
        
        # Step 3: Main loop - keep subtracting chunks
        while a >= b:
            temp = b
            multiple = 1
            
            # Double until we find the largest chunk that fits
            while a >= (temp << 1):
                temp <<= 1      # Double the value
                multiple <<= 1   # Double the multiple
            
            # Subtract the largest chunk
            a -= temp
            result += multiple
        
        # Step 4: Apply sign
        if negative:
            result = -result
        
        # Step 5: Handle 32-bit overflow
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        return result
