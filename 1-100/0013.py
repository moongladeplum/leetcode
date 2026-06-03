class Solution:
    def romanToInt(self, s: str) -> int:
        table = {"M" : 1000, "D" : 500, "C" : 100, "L" : 50, "X" : 10, "V" : 5, "I" : 1}
        summ, pre = 0, 'I'
        for c in s[::-1]:
            if table[c] < table [pre]:
                summ, pre = summ - table[c], c
            else:
                summ, pre = summ + table[c], c
        return summ
