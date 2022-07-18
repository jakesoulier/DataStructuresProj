
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

	# Use recursion until the correct position is found
	if key < node.key:
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)

	return node

def leftNode(node):
	current = node

	# loop down to find the leftmost value
	while(current.left is not None):
		current = current.left

	return current

def deleteNode(root, key):

	if root is None:
		return root

	if key < root.key:
		root.left = deleteNode(root.left, key)

	elif(key > root.key):
		root.right = deleteNode(root.right, key)

	else:

		if root.left is None:
			temp = root.right
			root = None
			return temp

		elif root.right is None:
			temp = root.left
			root = None
			return temp

		temp = leftNode(root.right)

		root.key = temp.key

		root.right = deleteNode(root.right, temp.key)

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
