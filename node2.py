class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def insert_node(node, key):
    if node is None:
        return Node(key)
    else:
        if node.value < key:
            node.right = insert_node(node.right, key)
        else:
            node.left = insert_node(node.left, key)
    return node


def search_for_node(node, key):
    if node.value == key:
        return True
    elif node is None:
        return False
    if node.value < key:
        if node.right is None:
            return False
        return search_for_node(node.right, key)
    else:
        if node.left is None:
            return False
        return search_for_node(node.left, key)


def in_order(node):
    if node:
        in_order(node.left)
        print(node.value)
        in_order(node.right)


def pre_order(node):
    if node:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)
