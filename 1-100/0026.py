class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Sort the array
        nums.sort()
        #Create a set of unique values    
        s = set(nums)
        #Unused variable      
        l = []
        #Clear the original array
        nums.clear()
        #Append unique values back
        for i in s:      
            nums.append(i)
        #Sort again
        nums.sort()
        #Return count of unique values
        return len(s)
