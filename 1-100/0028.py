class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hlen = len(haystack)
        nlen = len(needle)
        
        # If needle is empty or longer than haystack
        if nlen == 0:
            return 0
        if nlen > hlen:
            return -1
        
        # Slide a window of size nlen across haystack
        for i in range(hlen - nlen + 1):
            # Check if substring matches needle
            if haystack[i:i + nlen] == needle:
                return i
        
        return -1
