class Node():
        def __init__(self, data):
            self.data = data
            self.ref = None
class LinkedList():
    
    def __init__(self):
        """
        Creates an empty linked list.
        """
        self.start_node = None

    def traverse_list(self):
        if self.start_node is None: # checks if list is empty
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.data , " ") # prints linked list as a string
                n = n.ref

    def insertHead(self, element):
        """""
        Write code to insert new element into head of list
        """""
        # --- Problem 1 --- #
        pass

    def insertTail(self, element):
        """""
        Write code to insert new element into tail of list
        """""
        # --- Problem 2 --- #
        pass

    def insertAfter(self, target_element, new_element):
        """""
        Write code to insert new element into list after given element
        """""
        # --- Problem 3 --- #
        pass

linkedlist = LinkedList()
linkedlist.insertHead(2)
linkedlist.insertHead(4)
linkedlist.insertHead(1)
linkedlist.insertHead(6)
linkedlist.insertHead(7)
linkedlist.traverse_list()
# Answer should print:
# 7
# 6
# 1
# 4
# 2
print("-----End of problem 1-----")
linkedlist.insertTail(10)
linkedlist.traverse_list()
# Answer should print:
# 7
# 6
# 1
# 4
# 2
# 10
print("-----End of problem 2-----")
linkedlist.insertAfter(4, 8)
linkedlist.traverse_list()
# Answer should print:
# 7
# 6
# 1
# 4
# 8
# 2
# 10
print("-----End of problem 3-----")

