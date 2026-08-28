class BrowserHistory(object):

    def __init__(self, homepage):
        self.back_list=[]
        self.forward_list=[]
        self.current_address=homepage

#__init__中定义的闭包与所属方法：
        def make_mover(from_list, to_list):
            def mover(steps):
                steps = min(steps, len(from_list))
                for it in range(0, steps):
                    to_list.append(self.current_address)
                    self.current_address = from_list.pop()
                return self.current_address
            return mover

        self.back=make_mover(self.back_list, self.forward_list)
        self.forward=make_mover(self.forward_list, self.back_list)

    def visit(self, url):
        self.forward_list[:]=[]
        self.back_list.append(self.current_address)
        self.current_address=url

    # def back(self, steps):
    #     if steps>len(self.back_list):
    #         steps=len(self.back_list)
    #     for it in range(0,steps):
    #         self.forward_list.append(self.current_address)
    #         self.current_address=self.back_list.pop()
    #     return self.current_address
    #
    # def forward(self, steps):
    #     if steps>len(self.forward_list):
    #         steps=len(self.forward_list)
    #     for it in range(0,steps):
    #         self.back_list.append(self.current_address)
    #         self.current_address=self.forward_list.pop()
    #     return self.current_address

