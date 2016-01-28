# BFS similar 504 ms
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses<2 or len(prerequisites)<2:
            return True

        while 1:
            count = 0
            sink_nodes = [1]*numCourses

            for pair in prerequisites:
                sink_nodes[pair[0]] = 0

            for pair in prerequisites:
                if sink_nodes[pair[1]]:
                    count += 1
                    prerequisites.remove(pair)

            if prerequisites == []:
                return True

            #no sink vertex means cyclic
            elif count == 0:
                return False

# BFS, topological sort 112 ms
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        if numCourses<2 or len(prerequisites)<2:
            return True

        indegrees = [0]*numCourses
        adj_list = [[] for i in range(numCourses)]

        for pair in prerequisites:
            indegrees[pair[0]] += 1
            adj_list[pair[1]].append(pair[0])

        courses = range(numCourses)

        flag = True # has indegree==0 node

        while flag and len(courses):
            # remove_list = []
            flag = False

            for i in courses:
                if indegrees[i] == 0:
                    for nb in adj_list[i]:
                        indegrees[nb] -= 1
                    courses.remove(i)
                    flag = True

        if len(courses)==0:
            return True
        else:
            return False

# DFS, topological sort 60 ms
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses<2 or len(prerequisites)<2:
            return True

        adj_list = [[] for i in range(numCourses)]
        visit_list = [0]*numCourses

        for pair in prerequisites:
            adj_list[pair[1]].append(pair[0])

        for i in xrange(numCourses):
            if not self.doDFS(adj_list, visit_list, i):
                return False

        return True

    def doDFS(self, adj_list, visit_list, i):
        if visit_list[i]==-1:
            return False

        if visit_list[i]==1:
            return True

        visit_list[i] = -1

        for j in adj_list[i]:
            if not self.doDFS(adj_list, visit_list, j):
                return False

        visit_list[i] = 1

        return True