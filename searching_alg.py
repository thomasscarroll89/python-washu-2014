def linear_search(mylist, element):
	steps = 0
	for item in mylist:
		steps += 1
		if item==element:
			print steps
			return item
		print steps
		return None

mylist = [4, "a", "b", 1, "A", "/"]
linear_search(mylist, 4)
linear_search(mylist, "A")
linear_search(mylist, "/")

def binary_search(mylist, element):
	if len(mylist)==1:
		if mylist[0] == element:
			print "Element found"
		else:
			print "Element not found"
	if element <= mylist[len(mylist)/2]:
		mylist = mylist[0:len(mylist)/2]
		binary_search(mylist, element)
	elif element >= mylist[len(mylist)/2]:
		mylist = mylist[len(mylist)/2+1: len(mylist)-1]
		binary_search(mylist, element)

binary_search(mylist=[1, 2, 3, 4, 5, "a", "b", "c", "d"], element="a")
binary_search(mylist=[1, 2, 3, 4, 5, "a", "b", "c", "d"], element="b")
binary_search(mylist=[1, 2, 3, 4, 5, "a", "b", "c", "d"], element="c")
binary_search(mylist=[1, 2, 3, 4, 5, "a", "b", "c", "d"], element="d")
mylist = ["a", "b", "c", "d"]
print len(mylist)
print len(mylist)/2
print mylist[len(mylist)/2+1 : len(mylist)]
#binary_search(mylist=[1, 2, 3, 4, 5, "a", "b", "c", "d"], element="e")