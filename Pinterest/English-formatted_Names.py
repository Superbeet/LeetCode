# -*- coding: utf-8 -*- 

# list of names) and returns a string representing the English-formatted
# conjunction of those names.. more info on 1point3acres.com
#
# For example, given these names: ['Alice', 'Bob', 'Carlos', 'Diana'].
#
# The output would be: "Alice, Bob, Carlos and Diana"

def conjunctNames(names):
    names = filter(None, names) # filter all meaningless charactres
    line = ""
    length = len(names)
    for i in range(len(names)-1):
        if i == len(names)-2:
            line += names[i] +' and'
        else:
            line += names[i] +', '

    if line == "":
    	line += names[length-1]
    else:
    	line += ' ' + names[length-1]
    return line

assert conjunctNames(["", "ab"]) == 'ab'
assert conjunctNames(["ab", ""]) == 'ab'
assert conjunctNames(['alex', 'peter', 'jeremy', 'joseph']) == 'alex, peter, jeremy and joseph'
assert conjunctNames(['alex', 'peter']) == 'alex and peter'

# Once the above is working, we iterate on the problem by adding a second
# argument to our function.
# This new argument is called `limit` and controls the maximum number of names
# that should be displayed.  Any remaining items are "summarized" using the
# string "# more" (e.g. "Alice, Bob and 2 more" when `limit=2`)
def conjunctNames(names,li):
    names = filter(None, names) # filter all meaningless charactres
    line = ""
    length = len(names)
    limit = li

    num = length - li
    if num <= 0:
        limit = length-1

    for i in range(limit):
    	if names[i] == "":
    		continue

        if i == limit-1:
            line += names[i]+' and'
        else:
            line += names[i]+', '

    if line == "":
    	line += names[length-1]
    elif num > 0:
        line += ' ' + str(num)+' more'
    else:
        line += ' ' + names[length-1]

    return line

# print "[", conjunctNames(["ab"], 5),"]"
assert conjunctNames(["", "ab"], 5) == 'ab'
assert conjunctNames(["ab", ""], 5) == 'ab'
assert conjunctNames(['alex', 'peter', 'jeremy'], 2) == 'alex, peter and 1 more'
assert conjunctNames(['alex', 'peter', 'jeremy', 'joseph'], 2) == 'alex, peter and 2 more'
assert conjunctNames(['alex', 'peter', 'jeremy', 'joseph'], 3) == 'alex, peter, jeremy and 1 more'
assert conjunctNames(['alex', 'peter', 'jeremy', 'joseph'], 5) == 'alex, peter, jeremy and joseph'
assert conjunctNames(['alex', 'peter'], 5) == 'alex and peter'

# CODE READING（what's the purpose of this function） 
def getFieldToItemsDict(list_of_items, field_name):
    d = defaultdict(list)
    for item in list_of_items:
        d[getattr(item, field_name, None)].append(item)
        #d[item.field_name].append(item)
    return d


# find bug in this function, this is my corrected version, th bugs are some minor subscript bugs, note the edge cases
def sb(sorted_list, needle):
    def sb_internal(low, high):
        if not sorted_list:
            return None
        if low > high:
            return None

        pivot_pos = (low + high) / 2

        if pivot_pos >= len(sorted_list):
            return None
        elif pivot_pos < 0:
            return None

        pivot = sorted_list[pivot_pos]
        if needle == pivot:
            return pivot
        elif needle < pivot:
            return sb_internal(low, pivot_pos)
        else:
            return sb_internal(pivot_pos + 1, high)

    return sb_internal(0, len(sorted_list) - 1)

"""
2.二轮问了项目，preference,然后coding: code isBipartiteGraph,
注意robustness, graph can be not strongly connected.看代码习惯，
注意不让user有太多传进参数。这轮有点紧张，面得不好，跪了。
"""








