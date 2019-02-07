#!/usr/bin/python3


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
        is_root = False
        if not current_node:
            return False
        else:
            if current_node == self.root:
                is_root = True
            return self._delete(current_node, data, is_root)

    def _delete(self, current, data, is_root):
        if current.left is None and current.right is None:  # case 1: No child node
            current = None
        # case 2: One child node
        elif current.left is not None and current.right is None:
            current = current.left
        elif current.left is None and current.right is not None:
            current = current.right
        # case 3: Two child node -> find leftest node in right child node and replace it
        elif current.left is not None and current.right is not None:
            replace_node = self._get_replace_node(current, current.right)
            replace_node.left = current.left
            replace_node.right = current.right
            current = replace_node

        if is_root:
            self.root = current

        return True

    def _get_replace_node(self, parent, current):
        if current.left is None:
            parent.left = current.right
            current.right = None
            return current
        else:
            return self._get_replace_node(current, current.left)

    def pre_order_traverse(self):
        if self.root is None:
            print("No root")
        else:
            self._pre_order(self.root)

    def _pre_order(self, current):
        if current is None:
            pass
        else:
            print(current.data)
            self._pre_order(current.left)
            self._pre_order(current.right)

    def in_order_traverse(self):
        if self.root is None:
            print("No root")
        else:
            self._in_order(self.root)

    def _in_order(self, current):
        if current is None:
            pass
        else:
            self._in_order(current.left)
            print(current.data)
            self._in_order(current.right)

    def post_order_traverse(self):
        if self.root is None:
            print("No root")
        else:
            self._post_order(self.root)

    def _post_order(self, current):
        if current is None:
            pass
        else:
            self._post_order(current.left)
            self._post_order(current.right)
            print(current.data)

    def level_order_traverse(self):
        if self.root is None:
            print("No root")
        else:
            queue = [self.root]
            while queue:
                node = queue.pop(0)
                print(node.data)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)


def example():
    array = [13, 30, 16, 4, 42, 20, 25, 28, 10]
    bst = BinarySearchTree()
    for data in array:
        bst.insert(data)

    print(bst.search(20))
    print(bst.search(31))

    print(bst.delete(13))
    print(bst.delete(3))
    print(bst.search(13))
    # traversal
    print("pre-order traversal")
    bst.pre_order_traverse()
    print("in-order traversal")
    bst.in_order_traverse()
    print("post-order traversal")
    bst.post_order_traverse()
    print("level-order traversal")
    bst.level_order_traverse()


if __name__ == "__main__":
    example()
