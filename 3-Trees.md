# Trees
## Introduction
What are trees in a data structure and algorithmic definition?

Trees are a bit different from the past 2 topics that we have talked about. Instead of having the data organized in a linear matter like in queues and linked lists, trees use a hierarchy data structure to organize its data.  There are many different types of trees, the main type we are going to focus on today are binary trees.
## Implementation
First, understanding can be much easier when we think of real-world examples.  That way we can take new things we do not know and relate it to something we already realize.  Here is an example we can think of:

The easy real-life example is already in the word.  Trees!  A tree starts at the root or trunk at the ground then splits off into many different branches.  Let's think of another though.  Have you ever played the hot and cold game?  The game involves you looking for something but, you do not know where it already is. For every step you take, you are either told you are colder or hotter based on if you are closer or farther away from the destination you are attempting to reach.  Each step is a new branch. At the end, you created a tree of different possible decisions you could have made.  

Can you think of a real-life example of a tree?  Spend some time brainstorming some.

Here is an image of a binary tree:

![image](https://user-images.githubusercontent.com/97404870/179426223-d43e76c8-fcb6-427c-a628-56b3251da18c.png)


## Efficiency
The reason trees are so often used is because of how efficient it can be.  The worst case scenario Big O efficiency is O(n) but, if the tree is balanced the efficiency is O(log n).

## Recursion
Recursion, as you may know, is when a function calls itself. Let us look at an example for a review.  One use if for factorials.  A factorial is defined as the product of an integer and all the integers below it.  So, the factorial of 7 is 1 × 2 × 3 × 4 × 5 × 6 × 7.  That equals 5040.  Let’s solve this same problem using recursion.
```
def factorial(n):
    if n == 1:
       return n
    else:
       return (n * factorial(n-1))

number = 7
print(factorial(number))
```
## Problem to Solve

Use this code to start and write answers:

[Link to starting code](https://github.com/jakesoulier/DataStructuresProj/blob/main/trees.py)

The main task you need to complete:

* Create BST
* Add function to insert data
* Add function to delete data given a certain value

**Answer should output:**


[Link to solution](https://github.com/jakesoulier/DataStructuresProj/blob/main/trees-solution.py)

## Links to other pages

* [Welcome Page](https://github.com/jakesoulier/DataStructuresProj/blob/main/0-welcome.md)
* [Queues](https://github.com/jakesoulier/DataStructuresProj/blob/main/1-Queues.md)
* [Linked Lists](https://github.com/jakesoulier/DataStructuresProj/blob/main/2-LinkedList.md)

