class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        state = {i: "unvisited" for i in range(numCourses)}

        def dfs(course):
            if state[course] == "visiting":
                return True
            if state[course] == "visited":
                return False
        
            state[course] = "visiting"
            for prereq in graph[course]:
                if dfs(prereq):
                    return True

            state[course] = "visited"
            return False          


        for course in range(numCourses):
            if dfs(course):
                return False

        return True
                
            
        