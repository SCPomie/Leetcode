class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # Dictionary mapping each course to its prerequisites
        prevMap = {i: [] for i in range(numCourses)}
        for crs, prev in prerequisites:
            prevMap[crs].append(prev)

        # Track courses in the current DFS path to detect cycles
        visiting = set()

        # Track courses that have been fully processed
        completed = set()

        # Store the courses in a valid order
        res = []

        # Recursive DFS
        def dfs(crs):
            # If the course is in the current path, a cycle is detected
            if crs in visiting:
                return False

            # If already completed, no need to check again
            if crs in completed:
                return True

            # Add the course to the current DFS path
            visiting.add(crs)

            # Check all prerequisites, return False if a cycle is found
            for prev in prevMap[crs]:
                if not dfs(prev):
                    return False

            # Mark the course as fully processed
            completed.add(crs)

            # Remove the course from the current DFS path
            visiting.remove(crs)

            # Add the course after all its prerequisites are processed
            res.append(crs)

            return True

        # Check every course, return empty list if a cycle exists
        for c in range(numCourses):
            if not dfs(c):
                return []

        # Return the valid course ordering
        return res