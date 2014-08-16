class Node():
	def __init__(self, _value=None, _next=None): #Each node has a value and a next attribute; the value tells the actual value of the list at that node, while next is usually treated as another node, which has another value (the next value in the list) and a next attribute pointing to the next value. 
		self.value = _value
		self.next = _next
	def __str__(self):
		return str(self.value)
	def NaddNode(self, new_value):
		if self.next == None: #If the next node is the end of the list, add the new value as a new node
			self.next = Node(_value=new_value)
		else: #Otherwise, rerun the function on the next node in the list
			self.next.NaddNode(new_value)
	def NaddNodeAfter(self, new_value, after_node, node_number=1):
		if node_number < after_node: #If we haven't reached the right node yet, simply increment node_number (to keep track of where we are in the list) and run the function on the next node
			node_number += 1
			self.next.NaddNodeAfter(new_value, after_node, node_number=node_number)
		elif node_number == after_node: #When we reach the right node, create a new node with the new value, and simply save the old node's next attribute as the new next attribute
			old_next = self.next
			self.next = Node(_value=new_value, _next=old_next)
	def NremoveNode(self, node_to_remove, node_number=1):
		if node_number < node_to_remove: #If we haven't reached the right node yet, simply increment node_number (to keep track of where we are in the list) and run the function on the next node
			node_number += 1
			self.next.NremoveNode(node_to_remove=node_to_remove, node_number=node_number)
		elif node_number == node_to_remove: #When we reach the right node, redefine the current node's value/next attributes as those of the next node, essentially destroying the old node
			self.value = self.next.value
			self.next = self.next.next
	def NremoveNodesByValue(self, value):
		if self.value==value:
			if self.next != None: #When we're not dealing with the last element of a list
				self.value = self.next.value
				self.next = self.next.next
				if self.value!=value: #This is to catch cases where subsequent elements in the list have the same value
					self.next.NremoveNodesByValue(value=value) #When the next element doesn't have the same value, simply continue running the function
				else:
					self.NremoveNodesByValue(value=value) #When the next element does have the same value, run the function again on the same node since this node has now been redefined by the function
			else: #When we are dealing with last element of list:
				self.value = None
				self.next=None
		else: #When the value does not need to be removed, simply run the function on the next node
			self.next.NremoveNodesByValue(value=value)
	
class LinkedList():
	def __init__(self, value):
		self.head = Node(_value=value, _next=None)
		self.len = 1

	def length(self):
		return self.len
		
	def __str__(self):
		output = "["
		if self.len != 1:
			for i in range(0, self.len-1): #For every element in a list (except for the last one), add the value separated by a comma
				output += str(eval("self.head" + ".next"*i + ".value"))
				output += ", "
			output += str(eval("self.head" + ".next"*(self.len-1) + ".value"))
		elif self.len == 1: #This is used so we don't add a comma at the end of a list with only one element
			output += str(eval("self.head" + ".next"*(self.len-1) + ".value")) #For the last value in a list, add just the value but don't add a comma
		output += "]"
		print output
		return output

	def addNode(self, new_value):
		self.head.NaddNode(new_value)
		self.len += 1
		
	def addNodeAfter(self, new_value, after_node):
		self.head.NaddNodeAfter(new_value, after_node)
		self.len += 1

	def removeNode(self, node_to_remove):
		#ASSUMES THAT NODE_TO_REMOVE IS AN INTEGER INDICATING THE INDEX OF THE LIST THAT IS TO BE REMOVED
		self.head.NremoveNode(node_to_remove=node_to_remove)
		self.len -= 1

	def removeNodesByValue(self, value):
		subtract_one_more=False
		if eval("self.head" + ".next"*(self.len-1) + ".value") == value: #We use the subtract_one_more object to keep track of cases where the last element of a list was removed, and so we need to subtract an extra unit from the length of the list
			subtract_one_more=True
		self.head.NremoveNodesByValue(value=value)
		new_length=self.RecalculateLength(old_length=self.len) #see comments for RecalculateLength function; necessary because I don't know how to 
																#reassign the length function for the LinkedList class from within the Node class's function
		self.len = new_length
		if subtract_one_more:
			self.len -= 1
				
	def RecalculateLength(self, old_length): #Recalculates the length by adding up the numbers of nodes with values that do not equal None; used in the RemoveNodesByValue function
		new_length = 0
		for i in range(0, old_length-1):
			if eval("self.head" + ".next"*i) != None:
				new_length += 1
		return new_length
	
	def reverse(self):
		original_length = self.len
		for i in range(original_length-2, -1, -1): #Go through every element of the list (except the last element) and add it to the end of the list in reverse order
			new_value = eval("self.head" + ".next"*i + ".value") 
			print new_value
			self.addNode(new_value=new_value)
		for i in range(original_length-1, 0, -1): #Go through and remove the first half of the resulting list to complete the reversal
			self.removeNode(node_to_remove=i)	
		for i in range(0, original_length): #Get rid of elements (especially trailing elements) that had None values; this was a result of the RemoveNodesByValue function
			if eval("self.head" + ".next"*i + ".value")==None:
				self.removeNode(node_to_remove=i+1)
		self.len = original_length #reset the original length; necessary since we ran the addNode function, which automatically increments the length
		
x = LinkedList(1)
x.addNode(2)
x.addNode(3)
x.addNode(4)
x.addNode(6)
x.addNode(7)
x.addNode(8)
x.addNode(9)
str(x)
x.addNodeAfter(5, 4)
str(x)
x.removeNode(5)
str(x)
x.addNodeAfter(9, 4)
x.addNode(9)
str(x)
x.removeNodesByValue(value=9)
str(x)
x.reverse()
str(x)
