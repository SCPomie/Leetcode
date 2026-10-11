class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Dictionary mapping each course to its prerequisites
        prevMap = {i: [] for i in range(numCourses)}
        for crs, prev in prerequisites:
            prevMap[crs].append(prev)

        # Track courses in the current DFS path to detect cycles
        visiting = set()

        # Recursive DFS
        def dfs(crs):
            # If the course is already in the current path, a cycle is detected
            if crs in visiting:
                return False

            # Return True if no prerequisites or already verified
            if prevMap[crs] == []:
                return True

            # Add the course to the current DFS path
            visiting.add(crs)

            # Check all prerequisites; return False if any DFS detects a cycle
            for prev in prevMap[crs]:
                if not dfs(prev):
                    return False

            # Remove from current path and mark as verified
            visiting.remove(crs)
            prevMap[crs] = []
            return True

        # Check every course to ensure no cycles exist
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True