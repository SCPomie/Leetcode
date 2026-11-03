class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:

        def solve(segs):
            # Sort segments by their starting position
            segs.sort()
            n = len(segs)

            # res stores the maximum coins, cur stores fully included coins
            res = cur = 0

            # j points to the next segment to add
            j = 0

            # Try starting a window at each segment
            for i in range(n):
                # Calculate the right boundary of the k-sized window
                end = segs[i][0] + k - 1

                # Add all segments that fit completely inside the window
                while j < n and segs[j][1] <= end:
                    # Add the total coins from segment j
                    cur += (segs[j][1] - segs[j][0] + 1) * segs[j][2]
                    j += 1

                # Store coins from a partially included segment
                part = 0

                # Check if the next segment partially overlaps the window
                if j < n and segs[j][0] <= end:
                    # Count only the coins inside the window
                    part = (end - segs[j][0] + 1) * segs[j][2]

                # Update the maximum coins found
                res = max(res, cur + part)

                # Check if the current segment was added to cur
                if j > i:
                    # Remove the current segment before moving to the next window
                    cur -= (segs[i][1] - segs[i][0] + 1) * segs[i][2]
                else:
                    # Skip the current segment if it was never added
                    j = i + 1

            return res

        # Check windows starting at the beginning of segments
        a = solve([c[:] for c in coins])

        # Reverse coordinates to check windows ending at segment boundaries
        b = solve([[-r, -l, c] for l, r, c in coins])

        # Return the maximum coins from both directions
        return max(a, b)
                