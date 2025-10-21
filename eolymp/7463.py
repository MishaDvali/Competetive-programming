class Node:
    def __init__(self, val, depth):
        self.depth = depth
        self.left = None
        self.right = None
        self.val = val
    def print(self):
        print(self.depth, self.val)
        if self.left is not None:
            self.left.print()
        if self.right is not None:
            self.right.print()

class Tree:
    def __init__(self) -> None:
        self.head = None
        self.maxdepth = 0

    def insert(self, val):
        if self.head is None:
            self.head = Node(val, 1)
            self.maxdepth = 1
            return
        node = self.head
        while True:
            if val < node.val:
                if node.left is None:
                    node.left = Node(val, node.depth + 1)
                    self.maxdepth = max(node.depth+1, self.maxdepth)
                    return
                else:
                    node = node.left
                    continue
            if node.right is None:
                node.right = Node(val, node.depth + 1)
                self.maxdepth = max(self.maxdepth, node.depth+1)
                return
            node = node.right
    def print(self):
        self.head.print()

    




_ = input()
nodes = list(map(int, input().split()))
tree = Tree()
for node in nodes:
    tree.insert(node)
print(tree.maxdepth)
tree.print()
