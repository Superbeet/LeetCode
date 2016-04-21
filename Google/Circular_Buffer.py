from collections import deque

class CircularBuffer():
    def __init__(self, size):
        self.size = size
        self.start = 0
        self.end = 0
        self.length = 0
        self.elems = [None for i in range(self.size)]
    
    def __move_on(self, pos):
        next_pos = pos + 1
        if next_pos>=self.size-1:
            return next_pos-self.size
        else:
            return next_pos
    
    def push(self, val):
        if self.length==self.size:
            return "overflow"
        else:
            self.elems[self.end] = val
            self.end = self.__move_on(self.end)
            self.length += 1
            return True
            
    def pop(self):
        if self.is_empty():
            return "empty"
            
        val = self.elems[self.start]
        self.elems[self.start] = None
        self.length -= 1
        self.start = self.__move_on(self.start)
        return val
    
    def is_empty(self):
        return self.length == 0

def copy_buffer(res, des, i, j):
	pass
	
buffer = CircularBuffer(5)
print buffer.push(1)
print buffer.push(2)
print buffer.push(3)
print buffer.push(4)
print buffer.push(5)
print buffer.push(6)
print buffer.push(7)
print buffer.pop()
print buffer.pop()
print buffer.push(6)
print buffer.push(7)
print buffer.push(8)
print buffer.pop()
print buffer.pop()
print buffer.pop()
print buffer.pop()
print buffer.pop()
print buffer.pop()
print buffer.pop()
