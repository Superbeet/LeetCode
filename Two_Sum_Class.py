class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.queue = []
        self.hashtable = {}
        self.hashset = set()

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number in self.hashtable:
            self.hashtable[number] += 1
        else:
            self.hashtable[number] = 1
            self.queue.append(number)
        
        print self.hashtable
        
    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        if value in self.hashset:
            return True
            
        res = False
        for i in xrange(len(self.queue)):
            diff = value-self.queue[i]
            if diff in self.hashtable:
                if diff == self.queue[i]:
                    if self.hashtable[diff]>1:
                        res = True
                else:
                    res = True
        if res:
            self.hashset.add(value)
            return True

        return False
    
two = TwoSum()
two.add(0)
two.add(-1)
# two.add(1)
print two.find(0)
