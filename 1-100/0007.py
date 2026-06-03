class Solution:
    def reverse(self, x: int) -> int:
        rint = 0
        minimum, maximum = -(2**31), 2**31 - 1
        while x:
            if rint < minimum // 10 + 1 or rint > maximum // 10:
                return 0
            y = x % 10
            if x < 0 and y > 0:
                y -= 10
            rint = rint * 10 + y
            x = (x - y) // 10
        return rint
