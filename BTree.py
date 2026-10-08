class BTree:
    def __init__(self):
        self.tree = {}

    def insert(self, key, value):
        self.tree[key] = value

    def search(self, key):
        return self.tree.get(key, "Not Found")

    def display(self):
        for k, v in sorted(self.tree.items()):
            print(k, ":", v)

    def delete(self, key):
        if key in self.tree:
            del self.tree[key]
            print("Deleted Successfully")
        else:
            print("Key not Found")

    def minimum(self):
        return min(self.tree) if self.tree else "Empty"

    def maximum(self):
        return max(self.tree) if self.tree else "Empty"


bt = BTree()

while True:
    print("\n1.Insert")
    print("2.Search")
    print("3.Display")
    print("4.Delete")
    print("5.Minimum")
    print("6.Maximum")
    print("7.Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        key = input("Enter key: ")
        value = input("Enter value: ")
        bt.insert(key, value)
        print("Inserted successfully")

    elif ch == "2":
        key = input("Enter key: ")
        print("Value:", bt.search(key))

    elif ch == "3":
        print("Key-Value pairs:")
        bt.display()

    elif ch == "4":
        key = input("Enter key: ")
        bt.delete(key)

    elif ch == "5":
        print("Minimum:", bt.minimum())

    elif ch == "6":
        print("Maximum:", bt.maximum())

    elif ch == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
