class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        new_node=Node(data)
        if not self.root:
            self.root=new_node
            return
        curr=self.root
        while True:
            if data < curr.data:
                if curr.left is None:
                    curr.left=new_node
                    break
                curr=curr.left
            else:
                    if curr.right is None:
                        curr.right=new_node
                        break
                    curr=curr.right  
    def in_order(self,node): 
        if node:
            self.in_order(node.left)
            print(node.data,end=" ")
            self.in_order(node.right)
    def pre_order(self,node):
        if node:
            print(node.data,end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)
    def post_order(self,node): 
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data,end=" ")
tree=BinaryTree()
user_input=input("Enter numbers:")
for item in user_input.split():
    tree.insert(int(item))
print("\n-- Traversals--")
print("In_Order(sorted):",end=" ")
tree.in_order(tree.root)
print("\nPre_Order(Root First):",end=" ")
tree.pre_order(tree.root)
print("\nPost_Order(Root Last):",end=" ")
tree.post_order(tree.root)
print()
                    
