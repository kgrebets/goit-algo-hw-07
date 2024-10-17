class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

    def find_extreme(self, find_min=True):
        if self.root is None:
            return None
        return self._find_extreme_recursive(self.root, find_min)

    def _find_extreme_recursive(self, node, find_min):
        current_node = node
        while (current_node.left if find_min else current_node.right) is not None:
            current_node = current_node.left if find_min else current_node.right
        return current_node.data

    def find_min(self):
        return self.find_extreme(find_min=True)

    def find_max(self):
        return self.find_extreme(find_min=False)

    def find_sum(self):
        return self._find_sum_recursive(self.root)

    def _find_sum_recursive(self, node):
        if node is None:
            return 0
        return node.data + self._find_sum_recursive(node.left) + self._find_sum_recursive(node.right)


bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Найменше значення у дереві:", bst.find_min())
print("Найбільше значення у дереві:", bst.find_max())
print("Сума всіх значень у дереві:", bst.find_sum())
