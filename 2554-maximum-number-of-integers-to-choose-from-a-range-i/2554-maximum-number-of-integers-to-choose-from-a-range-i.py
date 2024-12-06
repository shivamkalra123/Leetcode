class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)  # Convert banned list to a set for O(1) lookup
        currSum = 0
        count = 0
        
        # Iterate over numbers from 1 to n and skip banned numbers
        for x in range(1, n + 1):
            if x not in banned_set:  # Only consider numbers not in the banned set
                if currSum + x <= maxSum:  # Check if the number can be included
                    currSum += x
                    count += 1
                else:
                    break  # No need to check further if we exceed maxSum
        
        return count
