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
    
    
"""""
Using a queue, create and edit a waitlist
"""""


loop = None
que = Queue()
while loop!= "q":
    
    print('e: enqueue person to waitlist')
    print('d: dequeue person from waitlist')
    print('q: quit')
    loop = input()
    if loop == "e":
        new_person = input()
        que.enqueue(new_person)
    elif loop == "d":
        if que.ifEmpty():
           print('no people left to remove to waitlist')
        else:
            que.dequeue()
            
    print(que.items)
    
    
