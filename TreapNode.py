class TreapNode:
    def __init__(self, label, priority):
        self.label = label
        self.priority = priority
        self.father = None
        self.leftChild = None
        self.rightChild = None

    def isLeftChild(self):
        if self.father:
            return self.father.leftChild is self
        else:
            return False

    def isRightChild(self):
        if self.father:
            return self.father.rightChild is self
        else:
            return False

    def setLeftChild(self, node):
        self.leftChild = node
        if node:
            node.father = self

    def setRightChild(self, node):
        self.rightChild = node
        if node:
            node.father = self

    def successor(self):
        if self.rightChild is None:
            return None
        else:
            currentNode = self.rightChild
            while currentNode.leftChild:
                currentNode = currentNode.leftChild
            return currentNode

    def softReplace(self, node2):  # dirty trick
        self.label = node2.label

    def predecessor(self):
        if self.leftChild is None:
            return None
        else:
            currentNode = self.leftChild
            while currentNode.rightChild:
                currentNode = currentNode.rightChild
            return currentNode

    def size(self):
        size = 0
        if self.leftChild:
            size += self.leftChild.size()
        if self.rightChild:
            size += self.rightChild.size()
        return size + 1

    def height(self):
        lh, rh = 0, 0
        if self.leftChild:
            lh = self.leftChild.height()
        if self.rightChild:
            rh = self.rightChild.height()
        return max(lh, rh) + 1

    def checkBSTProperty(self):
        leftProp = self.leftChild is None or self.leftChild.label < self.label
        rightProp = self.rightChild is None or self.rightChild.label > self.label
        return leftProp and rightProp

    def checkHeapProperty(self):
        leftProp = self.leftChild is None or self.leftChild.priority < self.priority
        rightProp = self.rightChild is None or self.rightChild.priority < self.priority
        return leftProp and rightProp

    def assertProperties(self, recursive):
        assert self.checkBSTProperty(), self
        assert self.checkHeapProperty(), self
        if (recursive):
            if self.leftChild:
                self.leftChild.assertProperties(recursive)
            if self.rightChild:
                self.rightChild.assertProperties(recursive)
        return True

    def __str__(self):
        string = ""
        string += "(" + str(self.label) + "," + str(self.priority) + ")"
        if self.leftChild:
            string += str(self.leftChild)
        else:
            string += "None"
        if self.rightChild:
            string += str(self.rightChild)
        else:
            string += "None"
        return string
