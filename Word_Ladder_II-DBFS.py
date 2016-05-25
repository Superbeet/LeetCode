import string

class Solution(object):
    # Solution using double BFS
    def findLadders(self, begin, end, words_list):

        def construct_paths(begin, end, graph, path, paths):
            if begin == end:
                paths.append(path)
                return

            if begin in graph:
                for elem in graph[begin]:
                    construct_paths(elem, end, graph, path + [elem], paths)

        def add_path(graph, word, neigh, is_forward):
            if is_forward:
                if word not in graph:
                    graph[word] = [neigh]
                else:
                    graph[word].append(neigh)
            else:
                if neigh not in graph:
                    graph[neigh] = [word]
                else:
                    graph[neigh].append(word)

        def bfs_level(forward_set, backward_set, graph, is_forward, words_set):
            found = False
            
            while forward_set and backward_set:
                if len(forward_set) == 0:
                    return False


                if len(forward_set) > len(backward_set):
                    forward_set, backward_set = backward_set, forward_set
                    is_forward = not is_forward

                for word in forward_set:
                    words_set.discard(word)

                next_set = set()

                while forward_set:
                    word = forward_set.pop()

                    for index in xrange(len(word)):
                        for c in "abcdefghijklmnopqrstuvwxyz":
                            neigh = word[:index] + c + word[index+1:]

                            if neigh in backward_set:
                                found = True
                                add_path(graph, word, neigh, is_forward)

                            elif neigh in words_set:
                                next_set.add(neigh)
                                add_path(graph, word, neigh, is_forward)

                forward_set = next_set

                if found:
                    break

            return found

        graph, path, paths = {}, [begin], []
        is_found = bfs_level(set([begin]), set([end]), graph, True, words_list)
        construct_paths(begin, end, graph, path, paths)
        return paths

sol = Solution()
print sol.findLadders("a","c",set(["a","b","c"]))
