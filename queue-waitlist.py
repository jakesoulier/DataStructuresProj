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
        """""
        Get input from the user on what new person will be added to the waitlist
        then, add them or enqueue them to the queue.
        """""
    elif loop == "d":
        """""
        Remove or dequeue first person from queue.
        Make sure to first check if the list is empty, 
        only dequeue if list is not empty.  If the queue is empty
        return: "No more people left on waitlist"
        """""
            
    print(que.items)
    
    
