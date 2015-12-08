class stack(object):
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)
        return True

    def peek(self):
        return self.stack[-1] 

    def pop(self):
        return self.stack.pop(-1)

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack)==0

    def __str__(self):
        return "%s" %self.stack

    def __repr__(self):
        return "%s" %self.stack