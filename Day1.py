#Given an array of integers nums and an integer target, return the indices of the two numbers such that their sum is equal to the target.

class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement], i]

            seen[nums[i]] = i


