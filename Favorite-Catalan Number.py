def generate_chords(n):
    def helper(points):
        if not points:  # No points left, return a trivial configuration
            return [[]]
        
        results = []
        for i in range(1, len(points), 2):  # Choose a pair of points for the first chord
            left = points[1:i]  # Points inside the chord
            right = points[i+1:]  # Points outside the chord
            
            # Recursive generation of all subproblems
            left_chords = helper(left)
            right_chords = helper(right)
            
            # Combine left and right subproblem solutions
            for l in left_chords:
                for r in right_chords:
                    results.append([(points[0], points[i])] + l + r)
        
        return results

    # Start with all points (2n points labeled 1, 2, ..., 2n)
    points = list(range(1, 2*n + 1))
    return helper(points)

# Example usage
n = 3
all_chords = generate_chords(n)
for i, chords in enumerate(all_chords, 1):
    print(f"Configuration {i}: {chords}")
