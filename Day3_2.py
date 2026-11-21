#Return True if any number appears more than once; otherwise return False

class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
