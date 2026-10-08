class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
head = None
while True:
    print("\n 1.Insert End 2.Delete Front 3.Display 4.Exit")
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
        if head is None:
            print("List Empty")
        else:
            head = head.next
            print("Deleted")
    elif ch==3:
        t = head
        while t:
            print(t.data,"<->",end="")
            t= t.next
        print("None")
    elif ch==4:
        print("Exit")
        break
    else:
        print("Invalid out")
    
