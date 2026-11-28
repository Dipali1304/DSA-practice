# Given an integer array nums and an integer k,
# return the total number of continuous subarrays whose sum equals k.

class Solution:
    def subarraySum(self, nums, k):
        count = 0
        prefix_sum = 0

        frequency = {0: 1}

        for num in nums:
            prefix_sum += num

            required = prefix_sum - k

            if required in frequency:
                count += frequency[required]

            frequency[prefix_sum] = frequency.get(prefix_sum, 0) + 1

        return count
