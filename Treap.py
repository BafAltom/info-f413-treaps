from TreapNode import *
import random

class Treap:
	def __init__(self, root):
		self.root = root

	# Interface

	def size(self):
		if (self.root == None):
			return 0
		else:
			return self.root.size()

	def search(self, value):
		# Usual BST search
		currentN = self.root
		while (currentN != None and currentN.label != value):
			if (currentN.label > value):
				currentN = currentN.leftChild
			else:
				currentN = currentN.rightChild
		return currentN

	def addNode(self, node): # node can be an actual node or a value
		if (type(node) != TreapNode):
			node = TreapNode(node, None)
		node.priority = self.newPriority()
		self.add_bst(node)
		while(node != self.root and node.priority > node.father.priority):
			if (node.isLeftChild):
				self.rightRot(node)
			else:
				self.leftRot(node)

	def delNode(self, node): # node can be an actual node or a value
		if (type(node) != TreapNode):
			node = self.search(node)
		if (node == None):
			return False
		else:
			f = node.father
			if (node.leftChild == None):
				if (f == None): # node was root
					self.root = node.rightChild
				elif (node.isLeftChild):
					f.leftChild = node.rightChild
				else:
					f.rightChild = node.rightChild
			elif (node.rightChild == None):
				if (f == None): # node was root
					self.Root = node.leftChild
				if (node.isLeftChild):
					f.leftChild = node.leftChild
				else:
					f.rightChild = node.leftChild
			else:
				# we can replace node with either its predecessor or its successor
				# Wikipedia says we should randomly choose between the two for best efficiency
				# "good implementations add inconsistency to this selection." - http://en.wikipedia.org/wiki/Binary_search_tree#Deletion
				goForSuccessor = (random.random() < 0.5)
				if (goForSuccessor):
					replacementNode = node.successor()
				else:
					replacementNode = node.predecessor()
				# If we just switch the nodes (normal BST behavior), the heap set of rules will be violated (priority < father.priority)
				# We fix that problem by just switching the label...
				# Better (?) solution would be to push down the replacement by rotations
				node.softReplace(replacementNode) # (see note above)
				self.delNode(replacementNode)

	# Implementation

	def newPriority(self):
		return random.randint(0,10000)

	def softReplace(self, node2): # dirty trick
		node.label = node2.label

	def add_bst(self, node):
		currentNode = self.root
		nextNode = self.root
		while(nextNode != None):
			currentNode = nextNode
			if (currentNode.label > node.label):
				nextNode = currentNode.leftChild
			elif (currentNode.label < node.label):
				nextNode = currentNode.rightChild
			else:
				raise("Added value already present in the BST")

		if (currentNode == None):
			print "ROOT WAS NONE"
			self.root = node
		elif (currentNode.label > node.label):
			currentNode.leftChild = node
		else:
			currentNode.rightChild = node
		node.father = currentNode

	def leftRot(self, c):

		# define notation
		b = c.father
		bFather = b.father
		sub1 = b.leftChild
		sub2 = c.leftChild
		sub3 = c.rightChild

		#make rotation
		if (self.root == b):
			bFather = None
			self.root = c
		elif(b.isLeftChild()):
			bFather.leftChild = c
		else:
			bFather.rightChild = c
		c.father = bFather
		c.leftChild = b
		b.father = c
		c.rightChild = sub3
		if (sub3 != None): sub3.father = c
		b.leftChild = sub1
		if (sub1 != None): sub1.father = b
		b.rightChild = sub2
		if (sub2 != None): sub2.father = b

	def rightRot(self, b):
		# define notation
		c = b.father
		cFather = c.father
		sub1 = b.leftChild
		sub2 = b.rightChild
		sub3 = c.rightChild

		#make rotation
		if (self.root == c):
			cFather = None
			self.root = b
		elif (c.isLeftChild()):
			cFather.leftChild = b
		else:
			cFather.rightChild = b
		b.father = cFather
		b.rightChild = c
		c.father = b
		b.leftChild = sub1
		if (sub1 != None): sub1.father = b
		b.rightChild = sub2
		if (sub2 != None): sub2.father = b
		c.rightChild = sub3
		if (sub3 != None): sub3.father = c
