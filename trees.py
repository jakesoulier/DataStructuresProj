
class Node:

	# Commences new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


# Prints data in tree in order
def inorder(root):
	if root is not None:
		inorder(root.left)
		print (root.key,end=" ")
		inorder(root.right)


def insert(node, key):

	if node is None:
		return Node(key)

    # ------- Problem 1 -------
	# Use recursion until you find the correct position
	
	return node

def leftNode(node):
	current = node

	# loop down to find the leftmost value
	while(current.left is not None):
		current = current.left

	return current

def deleteNode(root, key):

    # ------- Problem 2 -------
	"""""
    Using recursion, find the data point to delete.
    Delete that data point from the tree
    """""

	return root




root = None
root = insert(root, 8)
root = insert(root, 18)
root = insert(root, 2)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 20)
root = insert(root, 10)

print ("Data in order")
inorder(root)

print ("\nDelete 20")
root = deleteNode(root, 20)
print ("Data in order")
inorder(root)
