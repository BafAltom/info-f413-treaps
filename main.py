import random

from TreapNode import *
from Treap import *

t = Treap(None)

elements_in_treap = []
for i in range(10):
	print ""
	prob = random.random()
	if (prob < 0.75 or len(elements_in_treap) == 0):
		value = random.random()
		elements_in_treap.append(value)
		print "add", value
		t.addNode(value)
	else:
		elemPos = random.randint(0, len(elements_in_treap)-1)
		remove_elem = elements_in_treap[elemPos]
		print "del", remove_elem
		t.delNode(remove_elem)
		elements_in_treap.remove(remove_elem)
	print "treap : ", t.root
	print "theorical size", len(elements_in_treap)
	print "returned size", t.size()
	assert(len(elements_in_treap) == t.size())
	assert(t.root == None or t.root.father == None)
print "fini"