class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        array = sorted(nums1 + nums2)
        if len(array) % 2 == 0: return (array[len(array) // 2] + array[len(array) // 2 - 1]) / 2
        else: return array[len(array) // 2]
