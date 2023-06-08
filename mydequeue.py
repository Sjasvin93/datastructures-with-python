#------node class implementation-----------
class Node:

    def __init__(self, data):
        self.key = data
        self.next = None
        self.prev = None

class myDeque:

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def getSize(self):
        print(self.size)
    
    def getFront(self):
        if self.front == None:
            print("Queue is empty")
        else:
            print(self.front.key)

    def getRear(self):
        if self.rear == None:
            print("Queue is empty")
        else:
            print(self.rear.key)

    def insertFront(self, data):
        temp = Node(data)
        if self.front == None:
            self.front = temp
            self.rear = temp
        else:
            temp.next = self.front
            self.front.prev = temp
            self.front = temp
        self.size = self.size + 1

    def deleteFront(self):
        if self.front == None:
            print("Nothing to delete")
            return
        else:
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
        self.size = self.size - 1

    def insertRear(self, data):
        temp = Node(data)
        if self.rear == None:
            self.rear = temp
            self.front = temp
        else:
            self.rear.next = temp
            temp.prev = self.rear
            self.rear = temp
        self.size = self.size + 1

    def deleteRear(self):
        if self.rear == None:
            print("Nothing to print")
            return
        else:
            self.rear = self.rear.prev
            if self.rear == None:
                self.front = None
            else:
                self.rear.next = None
        self.size = self.size - 1

    def traverse(self):
        if self.front == None:
            print("Nothing to print")
        else:
            curr = self.front
            while curr != None:
                print(curr.key)
                curr = curr.next

d = myDeque()
d.insertFront(10)
d.insertFront(20)
d.insertRear(30)
d.insertRear(40)
d.insertFront(60)
d.traverse()
print("----------------")
d.deleteRear()
d.traverse()
print("-------------")
d.getSize()
d.getFront()
d.getRear()