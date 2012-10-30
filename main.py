import random

from TreapNode import *
from Treap import *

t = Treap(None)

elements_in_treap = []
for i in range(10000):
	prob = random.random()
	if (prob < 0.5 or len(elements_in_treap) == 0):
		value = random.random()
		elements_in_treap.append(value)
		t.addNode(value)
	else:
		elemPos = random.randint(0, len(elements_in_treap)-1)
		remove_elem = elements_in_treap[elemPos]
		t.delNode(remove_elem)
		elements_in_treap.remove(remove_elem)
	assert(len(elements_in_treap) == t.size())
	assert(t.root == None or t.root.father == None)
print "fini"