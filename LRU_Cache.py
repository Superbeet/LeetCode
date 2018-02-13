import time

class Node(object):
    def __init__(self, key, value, expiry):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        # TTL
        self.expiry = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = capacity
        self.tail = Node(-1,-1)
        self.head = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashtable = {} # key:node

    def __move_to_tail(self, cur_node):
        cur_node.next = self.tail
        self.tail.prev.next = cur_node
        cur_node.prev = self.tail.prev
        self.tail.prev = cur_node

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.hashtable:
            return -1

        cur_node = self.hashtable[key]
        cur_node.prev.next = cur_node.next
        cur_node.next.prev = cur_node.prev
        # TTL
        if cur_node.expiry <= time.time():
            return -1

        self.__move_to_tail(cur_node)
        return cur_node.value

    def set(self, key, value, expiry): # TTL
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.hashtable:
            node = self.hashtable[key]
            node.prev.next = node.next
            node.next.prev = node.prev

        elif len(self.hashtable) == self.size:
            del self.hashtable[self.head.next.key]
            self.head.next = self.head.next.next
            self.head.next.prev = self.head

        new_node = Node(key, value, expiry) # TTL
        self.hashtable[key] = new_node
        self.__move_to_tail(new_node)


"""
Basic
"""
class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = capacity
        self.tail = Node(-1,-1)
        self.head = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashtable = {} # key:node
        
    def __move_to_tail(self, cur_node):
        cur_node.next = self.tail
        self.tail.prev.next = cur_node
        cur_node.prev = self.tail.prev
        self.tail.prev = cur_node
        
    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.hashtable:
            return -1
        
        cur_node = self.hashtable[key]
        cur_node.prev.next = cur_node.next
        cur_node.next.prev = cur_node.prev
        
        self.__move_to_tail(cur_node)
        return cur_node.value

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.hashtable:
            node = self.hashtable[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            
        elif len(self.hashtable) == self.size:
            del self.hashtable[self.head.next.key]
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
        
        new_node = Node(key, value)
        self.hashtable[key] = new_node
        self.__move_to_tail(new_node)
        