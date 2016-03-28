

class Solution(object):

    def one_edit_distance_substring_pair(self, s):
        size = len(s)
        hashmap = {}
        res = []

        for v in xrange(1, size):
            for i in xrange(0, size-v+1):
                substr = s[i:i+v]
                for j in xrange(1, v+1):
                    new_substr = substr[:j]+substr[j+1:]
                    # if substr == "ac":
                    #     print "new_substr->%s" %(new_substr)
                    #     print substr[:j], substr[j+1:]
                    if new_substr in hashmap:
                        res.append(sorted([substr, new_substr]))

                        for org_str in hashmap[new_substr]:
                            res.append(sorted([substr, org_str]))
                    
                        hashmap[new_substr].add(substr)
                    
                    else:
                        hashmap[new_substr] = set([substr])

                hashmap[substr] = set()

                # print_hash(hashmap)

        return sorted(res)

def print_hash(hashmap):
    print "--------------------------"
    for k, v in hashmap.iteritems():
        print "%s->%s" %(k, v)


sol = Solution()
string = "acaba"
res = sol.one_edit_distance_substring_pair(string)
print res
new_res, dup_res = [], []
size =  len(res)
for i in xrange(0, size):
    if res[i] not in res[i+1:]:
        new_res.append(res[i])
    else:
        dup_res.append(res[i])
print "-------new_res--------"
print new_res
print "-------dup_res--------"
print dup_res
