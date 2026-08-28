class MyQueue(object):

    def __init__(self):
        self.stack_input=[]
        self.stack_output=[]

    def elem_transfer(self):
        if not self.stack_output:
            while self.stack_input:
                self.stack_output.append(self.stack_input.pop())

    def push(self, x):
        self.stack_input.append(x)

    def pop(self):
        self.elem_transfer()
        return self.stack_output.pop()

    def peek(self):
        self.elem_transfer()
        return self.stack_output[-1]

    def empty(self):
        self.elem_transfer()
        return not len(self.stack_output)>0

