from TreapNode import *
import random

class Treap:
	def __init__(self, root):
		self.root = root

	# Interface

	def __str__(self):
		return str(self.root)

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
		print "temp tree after add_bst", str(self)
		while(node != self.root and node.priority > node.father.priority):
			if (node.isLeftChild()):
				print "one rightrot"
				self.rightRot(node)
			elif(node.isRightChild()):
				print "one leftrot"
				self.leftRot(node)
			else:
				raise("This should not happen")

	def delNode(self, node): # node can be an actual node or a value
		if (type(node) != TreapNode):
			node = self.search(node)
		if (node == None):
			raise "delNode: value", str(node), "was not found in Treap"
		else:
			f = node.father
			if (node.leftChild == None):
				if (f == None): # node was root
					self.root = node.rightChild
				elif (node.isLeftChild()):
					f.leftChild = node.rightChild
				else:
					f.rightChild = node.rightChild
				if (node.rightChild != None):
					node.rightChild.father = f
			elif (node.rightChild == None):
				if (f == None): # node was root
					self.root = node.leftChild
				elif (node.isLeftChild()):
					f.leftChild = node.leftChild
				else:
					f.rightChild = node.leftChild
				if (node.leftChild != None):
					node.leftChild.father = f
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
			self.root = node
		elif (currentNode.label > node.label):
			currentNode.leftChild = node
		else:
			currentNode.rightChild = node
		node.father = currentNode

	# TREE ROTATIONS
	# Also known as : implementation hell
	# Notations come from : http://en.wikipedia.org/wiki/Tree_rotation

	def leftRot(self, Q):
		assert(Q.isRightChild())

		# notations
		P = Q.father
		A = P.leftChild
		B = Q.leftChild
		C = Q.rightChild
		Pf = P.father

		#rotation
		if (Pf != None):
			if (P.isLeftChild()):
				Pf.setLeftChild(Q)
			else:
				Pf.setRightChild(Q)
		else:
			self.root = Q
		Q.setLeftChild(P)
		P.setLeftChild(A)
		P.setRightChild(B)
		Q.setRightChild(C)

	def rightRot(self, P):
		assert(P.isLeftChild())

		#notations
		Q = P.father
		A = P.leftChild
		B = P.rightChild
		C = Q.rightChild
		Qf = Q.father

		#rotation
		if (Qf != None):
			if (Q.isLeftChild()):
				Qf.setLeftChild(P)
			else:
				Qf.setRightChild(P)
		else:
			self.root = P

		P.setRightChild(Q)
		P.setLeftChild(A)
		Q.setLeftChild(B)
		Q.setRightChild(C)