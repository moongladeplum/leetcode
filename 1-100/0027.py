class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # Left pointer
        j = len(nums) - 1  # Right pointer
        
        while i <= j:
            if nums[i] == val:
                # Swap with element from the end
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1
        
        return i
