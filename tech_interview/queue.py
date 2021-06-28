class Queue:
    def __init__(self):
        self.queue = []
    
    def dequeue(self):
        return self.queue.pop(0)

    def enqueue(self,item):
        self.queue.append(item)

    def printQueue(self):
        print(self.queue)

test = Queue()

test.enqueue(1)
test.enqueue(4)
test.enqueue(6)
test.enqueue(8)
test.enqueue(10)
test.dequeue()
test.printQueue()