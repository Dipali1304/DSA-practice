#Return an array where each element is the sum of all previous elements, including itself.

class Solution:
    def runningSum(self, nums):
        result = []
        total = 0

        for num in nums:
            total += num
            result.append(total)

        return result
