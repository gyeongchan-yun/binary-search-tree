class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, current, new):
        if current.data < new.data:
            if current.right is None:
                current.right = new
            else:
                self._insert(current.right, new)
        else:
            if current.left is None:
                current.left = new
            else:
                self._insert(current.left, new)

    def search(self, data):
        return False if not self._search(self.root, data) else True

    def _search(self, current, data):
        if current is None:
            return False
        if current.data == data:
            return current

        if current.data < data:
            return self._search(current.right, data)
        else:
            return self._search(current.left, data)

    def delete(self, data):
        current_node = self._search(self.root, data)
        if not current_node:
            return False
        else:
            return self._delete(current_node, data)

    def _delete(self, current, data):
        if current.left is None and current.right is None:  # case 1: No child node
            current = None
            return True
        # case 2: One child node
        elif current.left is not None and current.right is None:
            current = current.left
            return True
        elif current.left is None and current.right is not None:
            current = current.right
            return True
        # case 3: Two child node -> find leftest node in right child node and replace it
        elif current.left is not None and current.right is not None:
            replace_node = self._get_replace_node(current, current.right)
            replace_node.left = current.left
            replace_node.right = current.right
            current = replace_node
            return True

    def _get_replace_node(self, parent, current):
        if current.left is None:
            parent.left = current.right
            return current
        else:
            return self._get_replace_node(current, current.left)


def example():
    array = [13, 30, 16, 4, 42, 20, 25, 28, 10]
    bst = BinarySearchTree()
    for data in array:
        bst.insert(data)

    print(bst.search(20))
    print(bst.search(31))

    print(bst.delete(13))
    print(bst.delete(3))


if __name__ == "__main__":
    example()
