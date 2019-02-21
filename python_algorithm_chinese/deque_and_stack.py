class Node(object):
    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next

    def __str__(self):
      return  '<Node: value: {}, next={}, prev={}'\
      .format(self.value, self.next, self.prev)

    __repr__ =  __str__


class DoubleLinkedList(object):
    def __init__(self, maxsize = None):
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):
        if self.maxsize is not None and len(self)>self.maxsize:
            raise Exception('full')
        node = Node(value=value)
        tailnode = self.tailnode()

        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node

        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self)>self.maxsize:
            raise Exception('full')
        node = Node(value=value)

        if self.root.next is self.root: #empty list
            node.next = self.root
            node.prev = self.root
            self.root.prev = node
            self.root.next = node
        else:
            node.prev = self.root
            headnode = self.root.next
            node.next = headnode
            headnode.prev = node
            self.root.next = node

        self.length += 1

    def remove(self, node):
     if node is self.root:
         return
     else:
        node.prev.next = node.next
        node.next.prev = node.prev
     self.length -= 1
     return node

    def iter_node(self):
     if self.root.next is self.root:
         return
     curnode = self.root.next
     while curnode.next is not self.root:
         yield curnode
         curnode = curnode.next
     yield curnode

    def __iter__(self):
     for node in self.iter_node():
         yield node.value

    def iter_node_reverse(self):
     if self.root.prev is self.root:
         return
     curnode = self.root.prev
     while curnode.prev is not self.root:
         yield curnode
         curnode = curnode.prev
     yield curnode


class Deque(DoubleLinkedList):
    def pop(self):
        if len(self) ==0:
            raise Exception('empty')
        tailnode = self.tailnode()
        value = tailnode.value
        self.remove(tailnode)
        return value

    def popleft(self):
        if len(self)==0:
            raise Exception('empty')
        headnode = self.headnode()
        value = headnode.value
        self.remove(headnode)
        return value

class Stack():
    def __init__(self):
        self.deque = Deque() #collections.deque

    def push(self, value):
        return self.deque.append(value)

    def pop(self):
        return self.deque.pop()

    def __len__(self):
        return len(self.deque)

    def is_empty(self):
        return len(self) == 0

def test_slack():
    s = Stack()
    for i in range(3):
        s.push(i)

    assert len(s) == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.pop() == 0

    assert s.is_empty()

    import pytest
    with pytest.raises(Exception) as excinfo:
        s.pop()
    assert 'empty' in str(excinfo.value)
