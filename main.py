import math
import random

from TreapNode import *
from Treap import *

def test_random(t):
	elements_in_treap = []
	for i in range(5000):
		if (i % 100 == 0): print i, "/", 5000
		prob = random.random()
		if (prob < 0.6 or len(elements_in_treap) == 0):
			value = random.random()
			elements_in_treap.append(value)
			t.addNode(value)
		else:
			elemPos = random.randint(0, len(elements_in_treap)-1)
			remove_elem = elements_in_treap[elemPos]
			t.delNode(remove_elem)
			elements_in_treap.remove(remove_elem)
		assert(t.checkRep())
		assert(len(elements_in_treap) == t.size())
		assert(t.root == None or t.root.father == None)
		assert(t.height() <= len(elements_in_treap))
	print t.size(), "nodes"
	print "log_2_(n) = ", math.log(t.size(), 2)
	print "height", t.height()

	accessTime = 0
	number_of_tests = 1000
	for i in range(number_of_tests):
		elem = elements_in_treap[random.randint(0,len(elements_in_treap) - 1)]
		el, at = t.search(elem)
		assert (el.label == elem)
		accessTime += at
	print "avg number of comparisons : ", accessTime / float(number_of_tests)

def test_worst_case(t):
	for i in range(2000):
		if (i % 100 == 0): print i, "/", 2000
		t.addNode(i)
	print t.size(), t.height()

t = Treap(None)
test_random(t)