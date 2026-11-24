#Each kid has a certain number of candies. 
#You are also given extra candies. 
#Return a Boolean list indicating whether each kid can have the greatest number of candies after receiving all the extra candies.

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        result = []

        for candy in candies:
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result
