class RecentCounter(object):

    def __init__(self):
        self.ping_stack=[]
        self.range_stack=[]

    def ping(self, t):
        self.ping_stack.append(t)
        self.range_stack.append(t)
        while self.range_stack[-1]-self.range_stack[0]>3000:
            del self.range_stack[0]
        return len(self.range_stack)

