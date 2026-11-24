#you are given a 2D array where each row represents a customer's bank accounts. Find the maximum total wealth of any customer

class Solution:
    def maximumWealth(self, accounts):
        max_wealth = 0

        for customer in accounts:
            total = sum(customer)

            if total > max_wealth:
                max_wealth = total

        return max_wealth
