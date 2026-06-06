class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtracking(current, a, b):
            if a == n and b == n:
                result.append(current)
                return
            if a < n:
                current += '('
                backtracking(current, a + 1, b)
                current = current[:-1]
            if a > b:
                current += ')'
                backtracking(current, a, b + 1)
                current = current[:-1]
        result = []
        backtracking("", 0, 0)
        return result
