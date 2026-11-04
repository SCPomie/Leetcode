class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        #create a dictionary first
        preMap = {i : [] for i in range(numCourses)}

        #add each preequisite to the correct course
        for course, prev in prerequisites:
            preMap[course].append(prev)
        
        visit = set()

        def dfs(course):
            #if there is a cycle return false
            if course in visit:
                return False
            #add it to the visit
            visit.add(course)
            #loop through the preequisites
            for prev in preMap[course]:
                #if the dfs returns false then return false
                if not dfs(prev):
                    return False
            #remove the current course from visit
            visit.remove(course)
            #clear the [couse]
            preMap[course] = []
            #returns true
            
            return True

        #calls the dfs(courses) 
        for course in range(numCourses):
            if not dfs(course):
                return False
    
        return True