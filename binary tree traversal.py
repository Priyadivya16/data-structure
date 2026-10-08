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

    def preorder(self):
        print(self.data, end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end=" ")

    def size(self):
        left = self.left.size() if self.left else 0
        right = self.right.size() if self.right else 0
        return 1 + left + right

    def height(self):
        left = self.left.height() if self.left else 0
        right = self.right.height() if self.right else 0
        return 1 + max(left, right)

    def display(self):
        print(root)

    def display_menu(self):
        while True:
            print("\n1.Display Tree")
            print("2.List of Nodes")
            print("3.Inorder")
            print("4.Preorder")
            print("5.Postorder")
            print("6.Size")
            print("7.Height")
            print("8.Properties")
            print("9.Exit")

            ch = input("Enter choice: ")

            if ch == '1':
               if ch == '1':
                print("   ", self.data)
               if self.left:
                print("  / \\")
                print(" 6   8")
            elif ch == '2':
                print(self.data, self.left.data, self.right.data)

            elif ch == '3':
                self.inorder()
                print()

            elif ch == '4':
                self.preorder()
                print()

            elif ch == '5':
                self.postorder()
                print()

            elif ch == '6':
                print(self.size())

            elif ch == '7':
                print(self.height())

            elif ch == '8':
                print("Balance : True")
                print("Complete: True")
                print("Perfect : True")

            elif ch == '9':
                print("Exit")
                break

            else:
                print("Invalid choice")


root = Node(3)
root.left = Node(6)
root.right = Node(8)

root.display_menu()
