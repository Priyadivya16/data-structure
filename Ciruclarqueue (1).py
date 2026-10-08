import queue
q=queue.Queue(maxsize=3)
while True:
    print("\n1.Enqueue 2.Dequeue 3. Empty 4.Full 5.Size 6.Exit")
    ch=int(input("enter Choice:"))
    if ch==1:
        if not q.full():
            q.put(input("Enter element:"))
        else:
             print("Queue Full")
    elif ch==2:
        if not q.empty():
            print("Deleted:",q.get())
        else:
            print("Queue Empty")
            
    elif ch==3:
        print("Queue Empty" if q.empty() else "Queue Not Empty")
    elif ch==4:
        print("Queue Full" if q.empty() else "Queue not empty")
    elif ch==5:
        print("size:",q.qsize())
    elif ch==6:
        print("Exit")
    else:
        print("Invalid Choice")
