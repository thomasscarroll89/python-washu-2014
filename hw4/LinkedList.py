class Node():
	def __init__(self, _value=None, _next=None):
		self.value = _value
		self.next = _next
	def __str__(self):
		return str(self.value)
	def NaddNode(self, new_value):
		if self.next == None:
			self.next = Node(_value=new_value)
		else:
			self.next.NaddNode(new_value)
	def NaddNodeAfter(self, new_value, after_node, node_number=1):
		if node_number < after_node:
			node_number += 1
			self.next.NaddNodeAfter(new_value, after_node, node_number=node_number)
		elif node_number == after_node:
			old_next = self.next
			self.next = Node(_value=new_value, _next=old_next)
	def NremoveNode(self, node_to_remove, node_number=1):
		if node_number < node_to_remove:
			node_number += 1
			self.next.NremoveNode(node_to_remove=node_to_remove, node_number=node_number)
		elif node_number == node_to_remove:
			self.value = self.next.value
			self.next = self.next.next
	def NremoveNodesByValue(self, value, number_removed=0):
		if self.value==value:
			self.value = self.next.value
			self.next = self.next.next
			number_removed += 1
			if self.value!=value:
				self.next.NremoveNodesByValue(value=value, number_removed=number_removed)
			else:
				self.NremoveNodesByValue(value=value, number_removed=number_removed)
		else:
			self.next.NremoveNodesByValue(value=value, number_removed=number_removed)
	def RecalculateLength(self, new_length=1):
		while self.next!=None:
			new_length += 1
			self.next.RecalculateLength(new_length=new_length)
		return new_length

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
		self.head.NremoveNodesByValue(value=value)
		new_length=self.head.RecalculateLength()
		self.len = new_length
	
	
		
		
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

