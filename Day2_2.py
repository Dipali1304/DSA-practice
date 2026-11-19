#Given an integer array nums, move all zeros to the end while maintaining the relative order of non-zero elements.

class Solution:
    def moveZeroes(self, nums):
        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        while j < len(nums):
            nums[j] = 0
            j += 1
