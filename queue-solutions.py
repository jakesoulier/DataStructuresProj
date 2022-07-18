class Queue():
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        self.items.pop()
    def ifEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

q = Queue()
q.enqueue('name')
q.enqueue('date')
q.enqueue('age')
q.dequeue()
print(q.items)
print(q.ifEmpty())
len = q.size()
print(len)
q.enqueue(5)
print(q.items)
