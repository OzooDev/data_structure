"""
우선순위 큐(Priority Queue), 힙(Heap) 구현
"""

# 완전 이진 트리 구현
class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

    # def set_left_node(self, lnode):
    #     self.left = lnode
    #
    # def set_right_node(self, rnode):
    #     self.right = rnode

    def set_node(self, lnode, rnode):
        self.left = lnode
        self.right = rnode

    def check_empty(self):
        if self.left == None:
            # if self.
            pass

class BinaryTree:
    def __init__(self):
        self.root = None
        self.last_node = None

    def insert_node(self, item):
        new_node = Node(item)
        if self.root == None:
            self.root = new_node
            self.last_node = new_node
        else:
            pass

    def search_tree_index(self):
        pass
        # if self.root




bt = BinaryTree()
bt.