#-----node class implementation-------
class Node:

    def __init__(self, data):
        self.key = data
        self.next = None

class myQueue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def getSize(self):
        print(self.size)

    def getFront(self):
        print(self.front.key)
    
    def getRear(self):
        print(self.rear.key)

    def isEmpty(self):
        if self.size == 0:
            print("True")
        else:
            print("False")

    def enqueue(self, data):
        temp = Node(data)
        if self.front == None:
            self.front = temp
            self.rear = self.front
        else:
            self.rear.next = temp
            self.rear = temp
        self.size = self.size + 1

    def dequeue(self):
        if self.front == None:
            return
        else:
            self.front = self.front.next
            if self.front == None:
                self.rear = None
        self.size = self.size - 1

    def traverse(self):
        if self.front == None:
            print("Nothing to print")
        else:
            curr = self.front
            while curr != None:
                print(curr.key)
                curr = curr.next

q = myQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.traverse()
q.dequeue()
q.traverse()