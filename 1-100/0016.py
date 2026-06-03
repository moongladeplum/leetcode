class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = float('inf')

        for i in range(n - 2):
            x = nums[i]
            if i and x == nums[i - 1]:
                continue
            s = x + nums[i + 1] + nums[i + 2]
            if s > target:
                if s - target < abs(ans - target):
                    ans = s
                break
            s = x + nums[-2] + nums[-1]
            if s < target:
                if target - s < abs(ans - target):
                    ans = s
                continue
            j = i + 1
            k = n - 1
            s = x + nums[j] + nums[k]            
            while j < k:
                s = x + nums[j] + nums[k]
                if s == target:
                    return target
                if abs(s - target) < abs(ans - target):
                    ans = s
                if s > target:
                    k -= 1
                else:
                    j += 1
        return ans
