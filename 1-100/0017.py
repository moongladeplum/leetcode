class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        answer = [""]
        for i in digits:
            s = letters[int(i) - 2]
            answer = [a + b for a in answer for b in s]
        return answer
