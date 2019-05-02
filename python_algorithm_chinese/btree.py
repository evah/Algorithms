class BinTreeNode(object):

    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right


class BinTree(object):

    def __init__(self, root=None):
        self.root = root

    @classmethod # 使用@staticmethod或@classmethod，就可以不需要实例化，直接类名.方法名()来调用。
    def build_from(cls, node_list):
        node_dict = {}
        for node_data in node_list:
            data = node_data['data']
            node_dict[data] = BinTreeNode(data)
        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                root = node
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
        return cls(root)

    def preorder_trav(self, subtree):
        """先序遍历"""
        if subtree is not None:
            print(subtree.data)
            self.preorder_trav(subtree.left)
            self.preorder_trav(subtree.right)

    def inorder_trav(self, subtree):
        """中序遍历"""
        if subtree is not None:
            self.inorder_trav(subtree.left)
            print(subtree.data)
            self.inorder_trav(subtree.right)

    def postorder_trav(self, subtree):
        """后序遍历"""
        if subtree is not None:
            self.postorder_trav(subtree.left)
            self.postorder_trav(subtree.right)
            print(subtree.data)


node_list = [
    {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
    {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
    {'data': 'D', 'left': None, 'right': None, 'is_root': False},
    {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
    {'data': 'H', 'left': None, 'right': None, 'is_root': False},
    {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
    {'data': 'F', 'left': None, 'right': None, 'is_root': False},
    {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
    {'data': 'I', 'left': None, 'right': None, 'is_root': False},
    {'data': 'J', 'left': None, 'right': None, 'is_root': False},
]

btree = BinTree.build_from(node_list)

print("preorder travel:")
btree.preorder_trav(btree.root)
print("inorder travel:")
btree.inorder_trav(btree.root)
print("postorder travel:")
btree.postorder_trav(btree.root)