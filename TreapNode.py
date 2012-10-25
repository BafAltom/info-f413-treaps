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

	def successor(self):
		if (currentNode.rightChild == None):
			return None
		else:
			currentNode = self.rightChild
			while(currentNode.leftChild != None):
				currentNode = currentNode.leftChild
			return currentNode

	def predecessor(self):
		if (currentNode.leftChild == None):
			return None
		else:
			currentNode = self.leftChild
			while(currentNode.rightChild != None):
				currentNode = currentNode.rightChild
			return currentNode

	def size(self):
		size = 1
		if (self.leftChild != None):
			size += self.leftChild.size()
		if (self.rightChild != None):
			size += self.rightChild.size()
		return size

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