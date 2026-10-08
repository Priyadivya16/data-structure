class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def remove(root, data):
    if root is None:
        return None

    if data < root.data:
        root.left = remove(root.left, data)

    elif data > root.data:
        root.right = remove(root.right, data)

    else:
        if root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        temp = root.right
        while temp.left:
            temp = temp.left

        root.data = temp.data
        root.right = remove(root.right, temp.data)

    return root


root = None

root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 10)
root = insert(root, 25)
root = insert(root, 50)
print("AVL Tree")

print("Inorder:")
inorder(root)

print("\n\nRoot:", root.data)

root = remove(root, 30)

print("After Removing Root:")
inorder(root)
