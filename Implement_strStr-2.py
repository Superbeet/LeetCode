#coding=utf-8
"""
Input:
haystack = 'aabbaa'; needle='bb'
Output:
return = 'bbaa'

预处理不需要按照P的定义写成O(m^2)甚至O(m^3)的。
我们可以通过P[1],P[2],…,P[j-1]的值来获得P[j]的值。
对于刚才的B="ababacb"，假如我们已经求出了P[1],P[2],P[3]和P[4]，
看看我们应该怎么求出P[5]和P[6]。P[4]=2，那么P [5]显然等于P[4]+1，
因为由P[4]可以知道，B[1,2]已经和B[3,4]相等了，现在又有B[3]=B[5]，
所以P[5]可以由P[4] 后面加一个字符得到。P[6]也等于P[5]+1吗？
显然不是，因为B[ P[5]+1 ]<>B[6]。那么，我们要考虑“退一步”了。
我们考虑P[6]是否有可能由P[5]的情况所包含的子串得到，即是否P[6]=P[ P[5] ]+1。
这里想不通的话可以仔细看一下：
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
    	pass

    def get_partial_match_table(self, needle):
    	table = [0 for i in range(len(needle))]
    	length = len(needle)
    	table[0] = 0
    	k = 0

    	for i in range(1, length):

    		# print "needle_i[%s]->%s, needle_k[%s]->%s" %(i, needle[i], k, needle[k])
    		# print "table->%s" %(table)

    		while k>0 and needle[k] != needle[i]:
    			k = table[k-1]

    		if needle[k] == needle[i]:
    			k = k + 1
    			
    		print "table[%s] <- %s" %(i, k)
    		table[i] = k

    	return table

class Solution:
    def strStr(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1
        
        i = 0
        n = len(target)
        m = len(source)
        target_hash = self.create_hash_code(target)
        source_hash = self.create_hash_code(source[0:n])    
        
        for i in xrange(1, m - n + 2):
            if source_hash == target_hash and source[i - 1: i - 1 + n] == target:
                return i - 1
                
            if i < m - n + 1:
                source_hash = self.update_hash_code(source_hash, n, source[i - 1], source[i - 1 + n])
            
        return -1
    
    def create_hash_code(self, string):
        prime = 3
        hash_code = 0
        for i, c in enumerate(string):
            hash_code += ord(c)*(prime**i)
        return hash_code
        
    def update_hash_code(self, pre_hash_code, target_size, old_char, new_char):
        prime = 3
        new_hash_code = (pre_hash_code - ord(old_char))/prime + ord(new_char)*(prime**(target_size - 1))
        return new_hash_code

sol = Solution()
print sol.get_partial_match_table("ababacb")