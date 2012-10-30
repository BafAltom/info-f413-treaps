from TreapNode import *
import random

class Treap:
	MAX_PRIORITY = 10000
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

	def height(self):
		if (self.root == None):
			return 0
		else:
			return self.root.height()

	def checkRep(self):
		if (self.root == None):
			return True
		return self.root.assertProperties(True)

	def search(self, value):
		# Usual BST search
		currentN = self.root
		count = 1
		while (currentN != None and currentN.label != value):
			count += 1
			if (currentN.label > value):
				currentN = currentN.leftChild
			else:
				currentN = currentN.rightChild
		return currentN, count

	def addNode(self, node): # node can be an actual node or a value
		if (not isinstance(node, TreapNode)):
			node = TreapNode(node, None)
		node.priority = self.newPriority()
		while(self.isPriorityInTree(node.priority)):
			node.priority = (node.priority + 1)%(self.MAX_PRIORITY + 1)
		self.add_bst(node)
		while(node != self.root and node.priority >= node.father.priority):
			if (node.priority == node.father.priority):
				raise Exception("Priority", node.priority, "already exists in the tree!" + str(self))
			if (node.isLeftChild()):
				self.rightRot(node)
			elif(node.isRightChild()):
				self.leftRot(node)
			else:
				raise Exception("This should not happen")

	def delNode(self, node): # node can be an actual node or a value
		if (not isinstance(node, TreapNode)):
			value = node
			node, _ = self.search(value)
		else:
			value = node.label
		if (node == None):
			raise Exception("delNode: value " + str(value) + " was not found in Treap")
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
				self.delNode(replacementNode)
				node.softReplace(replacementNode) # (see note above)

	# Implementation

	def newPriority(self):
		return random.randint(0,self.MAX_PRIORITY)

	def isPriorityInTree(self, prio):
		return self.isPriorityUnderNode(prio, self.root)

	def isPriorityUnderNode(self, prio, node):
		if (node == None):
			return False
		localVerif = (node.priority == prio)
		if (node.priority > prio):
			localVerif = (localVerif or self.isPriorityUnderNode(prio, node.leftChild))
			localVerif = (localVerif or self.isPriorityUnderNode(prio, node.rightChild))
		return localVerif

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
				raise Exception("Added value already present in the BST")

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
		Q.father = Pf
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
		P.father = Qf
		P.setRightChild(Q)
		P.setLeftChild(A)
		Q.setLeftChild(B)
		Q.setRightChild(C)