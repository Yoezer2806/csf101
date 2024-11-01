class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a value into the BST
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    # Exercise 1: Find the maximum value in the BST
    def find_max(self):
        current = self.root
        while current and current.right:
            current = current.right
        return current.value if current else None

    # Exercise 2: Count the total number of nodes in the BST
    def count_nodes(self):
        return self._count_nodes_recursive(self.root)

    def _count_nodes_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)

    # Exercise 3: Level-order traversal (breadth-first search) for the BST
    def level_order_traversal(self):
        result = []
        queue = [self.root] if self.root else []
        while queue:
            current = queue.pop(0)
            result.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

    # Exercise 4: Find the height of the BST
    def find_height(self):
        return self._find_height_recursive(self.root)

    def _find_height_recursive(self, node):
        if node is None:
            return -1  # Base case: height of empty subtree
        left_height = self._find_height_recursive(node.left)
        right_height = self._find_height_recursive(node.right)
        return 1 + max(left_height, right_height)

    # Exercise 5: Check if the tree is a valid BST
    def is_valid_bst(self):
        return self._is_valid_bst_recursive(self.root, float('-inf'), float('inf'))

    def _is_valid_bst_recursive(self, node, min_val, max_val):
        if node is None:
            return True
        if node.value <= min_val or node.value >= max_val:
            return False
        return (self._is_valid_bst_recursive(node.left, min_val, node.value) and
                self._is_valid_bst_recursive(node.right, node.value, max_val))

    # Other methods for testing
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

# Testing the new methods
bst = BinarySearchTree()
for value in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(value)

print("In-order Traversal:", bst.inorder_traversal())
print("Maximum Value:", bst.find_max())
print("Total Nodes:", bst.count_nodes())
print("Level-order Traversal:", bst.level_order_traversal())
print("Height of BST:", bst.find_height())
print("Is Valid BST:", bst.is_valid_bst())
