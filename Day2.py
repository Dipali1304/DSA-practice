#Given an array of integers, find the second largest distinct element in the array.

class Solution:
    def secondLargest(self, nums):
        largest = float('-inf')
        second = float('-inf')

        for num in nums:
            if num > largest:
                second = largest
                largest = num

            elif num > second and num != largest:
                second = num

        if second == float('-inf'):
            return -1

        return second
