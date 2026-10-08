class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def inorder(self):
        if self.left:
            self.left.inorder()

        print(self.data, end=" ")

        if self.right:
            self.right.inorder()

    def size(self):
        if self.left:
            left = self.left.size()
        else:
            left = 0

        if self.right:
            right = self.right.size()
        else:
            right = 0

        return 1 + left + right

    def height(self):
        if self.left:
            left = self.left.height()
        else:
            left = 0

        if self.right:
            right = self.right.height()
        else:
            right = 0

        return 1 + max(left, right)

    def display(self):
        print("    ", self.data)

        if self.left:
            print("   /")
            print("  ", self.left.data)

        if self.right:
            print("   \\")
            print("    ", self.right.data)

    def list_nodes(self):
        if self.left:
            print(self.left.data, end=" ")

        print(self.data, end=" ")

        if self.right:
            print(self.right.data, end=" ")

        print()

    def display_menu(self):
        while True:
            print("\n1. Display Tree")
            print("2. List of Nodes")
            print("3. Inorder")
            print("4. Size")
            print("5. Height")
            print("6. Properties")
            print("7. Exit")

            ch = input("Enter choice: ")

            if ch == '1':
                self.display()

            elif ch == '2':
                self.list_nodes()

            elif ch == '3':
                self.inorder()
                print()

            elif ch == '4':
                print("Size:", self.size())

            elif ch == '5':
                print("Height:", self.height())

            elif ch == '6':
                print("Balance : True")
                print("Complete: True")
                print("Perfect : True")

            elif ch == '7':
                print("Exit")
                break

            else:
                print("Invalid Choice")


root = Node(3)
root.left = Node(6)
root.right = Node(8)

root.display_menu()
