class Solution(object):

    def decodeString(self, s):
        multi_stack=[]
        current_str=""
        current_num=0
        def read_char(char):
            nonlocal current_str,current_num,multi_stack
            if char.isdigit():
                current_num=current_num*10+int(char)
            elif char=="[":
                multi_stack.append([current_str,current_num])
                current_str=""
                current_num=0
            elif char=="]":
                pre_str,times=multi_stack.pop()
                current_str=pre_str+times*current_str
            else:
                current_str+=char

        for char in s:
            read_char(char)
        return current_str