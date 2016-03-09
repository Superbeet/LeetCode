# BFS by definition - topological sort 124 ms
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        if prerequisites==None:
            return []

        if len(prerequisites)==0:
            return range(0, numCourses)

        indegrees = [0]*numCourses
        adj_list = [[] for i in range(numCourses)]

        for pair in prerequisites:
            indegrees[pair[0]] += 1
            adj_list[pair[1]].append(pair[0])

        courses = range(numCourses)

        flag = True # has indegree==0 node

        seq = []

        while flag and len(courses):
            # remove_list = []
            flag = False

            for i in courses:
                if indegrees[i] == 0:
                    for nb in adj_list[i]:
                        indegrees[nb] -= 1
                    courses.remove(i)
                    seq.append(i)
                    flag = True

        if len(courses)==0:
            return seq
        else:
            return []

# DFS, find the cycle 70 ms
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        if prerequisites==None:
            return []

        if len(prerequisites)==0:
            return range(0, numCourses)

        adj_list = [[] for i in range(numCourses)]
        visit_list = [0]*numCourses
        stack = []

        for pair in prerequisites:
            adj_list[pair[1]].append(pair[0])

        for i in xrange(numCourses):
            if not self.doDFS(adj_list, visit_list, i, stack):
                return []

        return stack[::-1]

    def doDFS(self, adj_list, visit_list, i, stack):
        if visit_list[i]==-1:
            return False

        if visit_list[i]==1:
            return True

        visit_list[i] = -1

        for j in adj_list[i]:
            if not self.doDFS(adj_list, visit_list, j, stack):
                return False
        
        stack.append(i)

        visit_list[i] = 1

        return True