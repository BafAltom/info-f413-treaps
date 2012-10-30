class TreapNode:
	def __init__(self, label, priority):
		self.label = label
		self.priority = priority
		self.father = None
		self.leftChild = None
		self.rightChild = None

	def isLeftChild(self):
		if (self.father != None):
			return (self.father.leftChild == self)
		else:
			return False

	def isRightChild(self):
		if (self.father != None):
			return (self.father.rightChild == self)
		else:
			return False

	def setLeftChild(self, node):
		self.leftChild = node
		if (node != None):
			node.father = self

	def setRightChild(self, node):
		self.rightChild = node
		if (node != None):
			node.father = self

	def successor(self):
		if (self.rightChild == None):
			return None
		else:
			currentNode = self.rightChild
			while(currentNode.leftChild != None):
				currentNode = currentNode.leftChild
			return currentNode

	def softReplace(self, node2): # dirty trick
		self.label = node2.label

	def predecessor(self):
		if (self.leftChild == None):
			return None
		else:
			currentNode = self.leftChild
			while(currentNode.rightChild != None):
				currentNode = currentNode.rightChild
			return currentNode

	def size(self):
		size = 0
		if (self.leftChild != None):
			size += self.leftChild.size()
		if (self.rightChild != None):
			size += self.rightChild.size()
		return (1 + size)

	def height(self):
		lh, rh = 0, 0
		if (self.leftChild != None):
			lh = self.leftChild.height()
		if (self.rightChild != None):
			rh = self.rightChild.height()
		return (1 + max(lh, rh))

	def checkBSTProperty(self):
		leftProp = (self.leftChild == None or self.leftChild.label < self.label)
		rightProp = (self.rightChild == None or self.rightChild.label > self.label)
		return (leftProp and rightProp)

	def checkHeapProperty(self):
		leftProp = (self.leftChild == None or self.leftChild.priority < self.priority)
		rightProp = (self.rightChild == None or self.rightChild.priority < self.priority)
		return (leftProp and rightProp)

	def assertProperties(self, recursive):
		assert self.checkBSTProperty(), self
		assert self.checkHeapProperty(), self
		if (recursive):
			if (self.leftChild != None): self.leftChild.assertProperties(recursive)
			if (self.rightChild != None): self.rightChild.assertProperties(recursive)
		return True

	def __str__(self):
		string = ""
		string += "(" + str(self.label) + "," + str(self.priority) + ")"
		if (self.leftChild != None):
			string += str(self.leftChild)
		else:
			string += "None"
		if (self.rightChild != None):
			string += str(self.rightChild)
		else:
			string += "None"
		return string