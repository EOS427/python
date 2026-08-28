class DoubleLinkedNode(object):
    def __init__(self,key=None,value=None,front=None,next=None):
        self.key=key
        self.value = value
        self.front=front
        self.next = next


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = DoubleLinkedNode()
        self.tail = DoubleLinkedNode()
        self.head.next = self.tail
        self.tail.front = self.head

    def get(self, key):
        if key in self.cache:
            node=self.cache[key]
            self.list_prepose_node(node)
            return node.value
        else:return -1


    def put(self, key, value):
        if key in self.cache:
            node=self.cache[key]
            node.value=value
            self.list_prepose_node(node)
        else:
            node = DoubleLinkedNode(value=value,key=key)
            self.cache[key] = node
            self.list_head_insert(node)
            if len(self.cache)>self.capacity:
                longest_not_use_node=self.list_delete_tail()
                del self.cache[longest_not_use_node.key]


    def list_head_insert(self, node):
        node.front = self.head
        node.next = self.head.next
        self.head.next.front = node
        self.head.next = node

    def list_separate_node(self, node):
        front_node=node.front
        next_node=node.next
        front_node.next=next_node
        next_node.front=front_node

    def list_prepose_node(self, node):
        self.list_separate_node(node)
        self.list_head_insert(node)

    def list_delete_tail(self):
        longest_not_use_node=self.tail.front
        self.list_separate_node(longest_not_use_node)
        return longest_not_use_node