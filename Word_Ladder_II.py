class Solution2:
    def findLadders(self, start, end, dict):
        # DFS to retrive the path
        def buildpath(graph, path, word, result):
            if word not in graph:
                curr_path = path[::-1]
                result.append(curr_path)
                return
            for next_word in graph[word]:
                path.append(next_word)
                buildpath(graph, path, next_word, result)
                path.pop()
        
        graph={}
        current = set([start])
        previous = set()

        while True:
            current, previous = previous, current
            for i in previous: 
                dict.remove(i)
            current.clear()

            for word in previous:
                for i in xrange(len(start)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i] != c:
                            new_word = word[:i] + c + word[i+1:]
                            if new_word in dict:
                                if new_word not in graph:
                                    graph[new_word] = [word]
                                else:
                                    graph[new_word].append(word)
                                current.add(new_word)

            if len(current)==0: 
                return []

            if end in current: 
                break

        result = []
        buildpath(graph, [end], end, result)
        return result

# import copy

# class Solution:

#     def buildpath(self, graph, path, start_word, word, result, depth, max_depth):
#         # print "path-> %s" %(path)
#         # print "word-> %s" %(word)
#         if depth>max_depth:
#             return 

#         if word == start_word:
#             # print start_word
#             # print path
#             result.append(copy.deepcopy(path))
#             # print "result-> %s" %(result)
#             return

#         if word not in graph:
#             return

#         for next_word in graph[word]:
#             if next_word not in path:
#                 path.append(next_word)
#                 self.buildpath(graph, path, start_word, next_word, result, depth+1, max_depth)
#                 path.pop()
#         return

#     def findLadders(self, start, end, dict):
#         # DFS to retrive the path
#         graph={}
#         forward = set([start]); forward_check = set([])
#         backward = set([end]); backward_check = set([])

#         found = False
#         count = 1
#         while forward and backward:
#             if len(forward) > len(backward):
#                 forward, backward = backward, forward
#                 forward_check, backward_check = backward_check, forward_check
#             # print is_forward, forward, backward
#             temp = set()
#             for word in forward:
#                 for i in xrange(len(word)):
#                     for letter in 'abcdefghijklmnopqrstuvwxyz':
#                         if word[i] != letter:
#                             new_word = word[:i] + letter + word[i+1:]
#                             if new_word in backward:
#                                 found = True
#                             if new_word not in forward_check and new_word in dict:
#                                 forward_check.add(new_word)
#                                 temp.add(new_word)
#                             # if is_forward:
#                                 if new_word not in graph:
#                                     graph[new_word] = set([word])
#                                 else:
#                                     graph[new_word].add(word)
#                             # else:
#                                 if word not in graph:
#                                     graph[word] = set([new_word])
#                                 else:
#                                     graph[word].add(new_word) 
#             forward = temp
#             count += 1
#             if found:
#                 break
#         print "graph->", graph
#         result = []
#         self.buildpath(graph, [end], start, end, result, 0, count)
#         return result


sol = Solution()
# sol2 = Solution2()
# bw = "hot"
# ew = "dog"
# wl = set(["hot","cog","dog","tot","hog","hop","pot","dot"])

begin = "hit"
end = "cog"
dictbook = set(["hot","cog","dot","dog","hit","lot","log"])

begin = "red"
end = "tax"
dictbook = set(["ted","tex","red","tax","tad","den","rex","pee"])
print sol.findLadders(begin, end, dictbook)
# print sol2.findLadders(bw, ew, wl)

