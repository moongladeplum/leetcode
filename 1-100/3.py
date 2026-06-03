class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapset = {}
        start, result = 0, 0
        for end in range(len(s)):
            if s[end] in mapset:
                start = max(mapset[s[end]], start)
            result = max(result, end-start+1)
            mapset[s[end]] = end+1
        return result
