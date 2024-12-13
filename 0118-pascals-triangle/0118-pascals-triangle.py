class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        memo = {}  # Dictionary to store precomputed rows

        def solve(row):
            # Check if the row is already computed
            if row in memo:
                return memo[row]

            if row == 1:  # Base case: First row is always [1]
                memo[row] = [1]
            else:
                # Recursive call to get the previous row
                prev_row = solve(row - 1)

                # Build the current row using the previous row
                current_row = [1]  # First element is always 1
                for i in range(1, len(prev_row)):
                    current_row.append(prev_row[i - 1] + prev_row[i])  # Sum of two adjacent elements
                current_row.append(1)  # Last element is always 1

                # Store the computed row in the memo dictionary
                memo[row] = current_row
            
            return memo[row]

        # Generate all rows up to numRows
        result = []
        for i in range(1, numRows + 1):
            result.append(solve(i))
        
        return result
