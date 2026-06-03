class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(left, right):
            while 0 <= left <= right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        palindrome = [check(i, i) for i in range(len(s))] + [check(i, i + 1) for i in range(len(s) - 1) if s[i] == s[i + 1]]
        return sorted(palindrome, key = len)[-1] if palindrome else ''
