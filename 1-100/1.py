class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i, x in enumerate(nums):
            if (y := target - x) in sums:
                return [sums[y], i]
            sums[x] = i
