#Every element appears twice except one. Find the element that appears only once.

class Solution:
    def singleNumber(self, nums):
        result = 0

        for num in nums:
            result ^= num

        return result
