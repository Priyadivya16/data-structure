class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def display_right_root_left(self,node):
        if node:
            self.display_right_root_left(node.right)
            print(node.data,end=" ")
            self.display_right_root_left(node.left)
    def display_left_root_right(self,node):
        if node:
            self.display_left_root_right(node.left)
            print(node.data,end=" ")
            self.display_left_root_right(node.right)
    
    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_rec(self.root,data)
    def _insert_rec(self,node,data):
        if node.left is None:
            node.left = Node(data)
        elif node.right is None:
            node.right = Node(data)
        else:
            self._insert_rec(node.left,data)
    def delete_root(self):
        self.root = None
    def menu(self):
        while True:
            print("\n1.Display 2.Insert Front 3. Insert End 4. Delete root 5.exit")
            
            ch = input("Enter choice:")
            if ch =='1':
                print("Right-Root-Left:",end=" ")
                self.display_right_root_left(self.root)
                print()
                print("Left-Root-Right:",end=" ")
                self.display_left_root_right(self.root)
                print()
            elif ch == '2' or ch == '3':
                self.insert(int(input("Enter element:")))
            elif ch == '4':
                self.delete_root()
                print("Root delete")
            elif ch =='5':
                print("Exit")
                break
            else:
                print("INvalid choice")
bt = BinaryTree()
bt.menu()


                
