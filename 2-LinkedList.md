# Linked List
## Introduction
What is a Linked List?

They are also called a one way ordered list.  That is exactly what they are, an ordered group of elements that have a connection to each value next in line.  Basically, it is a linear order set of elements that connect each other with pointers.
## Implementation
Let's think of a real-world example of a linked list.  This always helps me understand principles and see the importance of them.  Maybe you will start to see examples of linked lists in your day-to-day life!  Here's a real-life example:

Imagine you are listening to your music library on shuffle.  Each time you skip or finish a song, a new, random song starts to play and is added to a linked list.  The last song points to your new song.  If you listen to multiple songs, you can go back a couple songs to one you were previously enjoying by pressing reverse and going back song by song.  All the previous songs are still pointed to each other.  Another reason this is a linked list is the new song is not added until you finish your current song, just like a linked list.  They have data added to them at runtime.  

Here is an image example of a linked list:

![image](https://user-images.githubusercontent.com/97404870/178087458-414074c7-791b-4057-b27e-dcc7448bc061.png)


## Efficiency
Linked list uses sequential access.  This is just a term that means data is accessed with some type of preset, ordered by retrieving form.  Since linked lists are accessed this way and are already linearly organized the big O efficiency is O(n).  The big O efficiency is different for linked list when you are inserting data or deleting data.  Since, with linked list, you will always add data from the end of the list and delete data from the start, you are not running through every point of the list.  You are going straight to the end or straight to the start.  This means the big O efficiency for inserting and deleting data is O(1).


## Problem to Solve

Use this code to start and write answers:

[Link to starting code](https://github.com/jakesoulier/DataStructuresProj/blob/main/linkedLists.py)

There are 3 main task you need to complete:

* Insert data into head of list
* Insert data into tail of list
* Insert data into list after another list element

**Answer should output:**


[Link to solution](https://github.com/jakesoulier/DataStructuresProj/blob/main/linkedList-solution.py)


## Links to other pages

[Welcome Page Link](https://github.com/jakesoulier/DataStructuresProj/blob/main/0-welcome.md)

[Queues](https://github.com/jakesoulier/DataStructuresProj/blob/main/1-Queues.md)

[Trees](https://github.com/jakesoulier/DataStructuresProj/blob/main/3-Trees.md)


