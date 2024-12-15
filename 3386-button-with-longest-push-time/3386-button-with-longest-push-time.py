class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        # Calculate press durations
        dp = [0] * len(events)  # Array to store durations
        dp[0] = events[0][1]  # First button's duration is its release time

        # Calculate durations for subsequent events
        for j in range(1, len(events)):
            dp[j] = events[j][1] - events[j-1][1]  # Time difference
        max_duration = max(dp)
        buttons_with_max_duration = [
            events[i][0] for i in range(len(dp)) if dp[i] == max_duration
        ]
        return min(buttons_with_max_duration)

        

        


        