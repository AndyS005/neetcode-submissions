class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for course, preq in prerequisites:
            graph[course].append(preq) 

        state = {i: "unvisited" for i in range(len(graph))}

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


        for course in graph:
            if dfs(course):
                return False

        return True
            

    
        
            
        