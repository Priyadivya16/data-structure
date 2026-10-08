class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
head = None
while True:
    print("\n 1.Insert End 2. Insert Front 3.Delete Front 4.Display 5.Exit")
    ch=int(input("Enter Choice:"))
    if ch==1:
        n=Node(input("Enter data:"))
        if head is None:
            head = n
        else:
            t = head
            while t.next:
                t=t.next
            t.next = n
    elif ch==2:
        n=Node(input("Enter data:"))
        n.next = head
        head = n
    elif ch==3:
        if head is None:
            print("List Empty")
        else:
            head = head.next
            print("Node Deleted")
    elif ch==4:
        t = head
        while t:
            print(t.data,"->",end="")
            t= t.next
        print("None")
    elif ch==5:
        print("Exit")
        break
    else:
        print("Invalid out")
    
