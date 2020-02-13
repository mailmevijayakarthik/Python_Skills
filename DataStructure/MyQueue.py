class myQueue:
    def __init__(self):
        self.queue=[]
    def isEmpty(self):
        return self.queue==[]
    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        data=self.queue[0]
        del self.queue[0]
        return data
    def peep(self):
        return self.queue[0]


queue=myQueue()
print(queue.isEmpty())
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)
print(queue.peep())
print(queue.dequeue())

