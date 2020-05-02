# Given an array nums, write a function to move all 0's to the 
# end of it while maintaining the relative order of the non-zero elements.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in nums:
            if i != 0:
                nums[index] = i
                index = index + 1
        #end for
        for j in range(index, len(nums)):
            nums[j] = 0
            