class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, x):
        self.stack.append(x)
        if len(self.minStack)==0 or x<=self.minStack[-1]:
            self.minStack.append(x)
 
    def pop(self):
        top = self.stack.pop()
        if top == self.minStack[-1]:
            self.minStack.pop()
        
    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]
