# Given a sorted array of integers numbers and a target value, 
# find two numbers whose sum equals the target. 
# Return their 1-based indices.

class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]

            elif total < target:
                left += 1

            else:
                right -= 1
