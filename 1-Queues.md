# Queues
## Introduction
What is a Queue?
A queue is form of data structure in programming.  It is a group of data elements where only the first part of the data can be accessed, and new elements are adding at the back.  The order is FIFO or first in, first out.
## Implementation
Can you think of any real-world examples of a queue?  Let me give you one to get you started.  When you go to the sandwich shop, you have to get in line to wait for your order.  You join at the back of the line.  That's where data is inserted for a queue.  Who gets served first?  That would be the first person in line.  When someone joins the line at the back, that is called enqueue.  When the person in the front is served and they leave the line, that is called dequeue.  They are the first out.  This is a fair and organized way and that is how it is used in a programming environment.

Here is an image example of a queue:

![image](https://user-images.githubusercontent.com/97404870/176754026-09319f32-78d1-4a97-bc70-e36ee7c36acf.png)

How do you use it in programming?  Specifically Python.

| Action | Description | Python syntax |
|---|---|---|
| Enqueue  | Adding value to back of queue  |  queue.append(value) |  
| Dequeue  | Removing first value of queue  | queue.pop()  |


## Deque
Deque, also called Double Ended Queue, is a type of Queue that allows of removal and insertion of elements can be done at the back or front of a collection of data.  This means it does not follow the first in first out rule.  Deque is often used more due to efficiency and performance.  There are a couple of different main operations inside of Deque.  Here they are:

**insertFront()**

**insertBack()**

**deleteFront()**

**deleteBack()**
## Effeciency
Queues are similar to linked list in their big O efficiency.  The data is not randomly accessed because it is organized sequentially.  This means the big O efficiency for searching and accessing certain data points is O(n) while the efficiency for adding or deleting values is O(1).

## Problem to Solve
Write a class and call it Queue.  Have a method that creates an empty queue when the class is called.  Inside the class make 5 different functions with these specific names:

**enqueue** - takes a value and adds it to the end of the queue

**dequeue** - removes first value of queue

**ifEmpty** - returns true if queue is empty and false if queue has values

**size** - returns length of queue

### Add this code to the bottom of your program to test it:
q = Queue()

q.enqueue('name')

q.enqueue('date')

q.enqueue('age')

q.dequeue()

q.ifEmpty()

len = q.size()

result = q.enqueue(5)

print(result)

**Answer should output:**

    2
    
    ['name', 'date', 5]

[Link to solution](https://github.com/jakesoulier/DataStructuresProj/blob/main/queue-solutions.py)

### Problem #2
Create a waitlist that can be added to and have people removable from the list.

Download this code to get started:

[Waitlist Problem](https://github.com/jakesoulier/DataStructuresProj/blob/main/queue-waitlist.py)

Do your best to complete this without looking at the solution.  When you are finished, you are free to compare it to the solution here:

[Waitlist Solution](https://github.com/jakesoulier/DataStructuresProj/blob/main/queue-waitlist-solution.py)

## Links to other pages

[Welcome Page Link](https://github.com/jakesoulier/DataStructuresProj/blob/main/0-welcome.md)

[Linked Lists](https://github.com/jakesoulier/DataStructuresProj/blob/main/2-LinkedList.md)

[Trees](https://github.com/jakesoulier/DataStructuresProj/blob/main/3-Trees.md)


