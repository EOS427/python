class MinStack(object):

    def __init__(self):
        self.current_stack=[]
        self.min_condition=[]

    def push(self, value):
        self.current_stack.append(value)
        if len(self.min_condition)==0:
            self.min_condition.append(value)
        else:
            if value<self.min_condition[-1]:
                self.min_condition.append(value)
            else:
                self.min_condition.append(self.min_condition[-1])

    def pop(self):
        self.current_stack.pop()
        self.min_condition.pop()

    def top(self):
        return self.current_stack[-1]

    def getMin(self):
        return self.min_condition[-1]
