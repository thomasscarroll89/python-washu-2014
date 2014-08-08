class School():
	def __init__(self, name):
		self.name = name
		self.db = {}
		
	def db(self):
		return self.db
	
	def add(self, student_name, grade):
		print "Add " + student_name + " to grade " + str(grade) + "."
		grade = int(grade) #in case grade is put in as a string, we convert it to an integer
		keys = self.db.keys() #gets a list of every grade that already has a student in it
		if grade in keys:
			old_roster = self.db[grade] #old_roster is a set; note that a set can be written as {stuff} or ([stuff]), and these are considered equivalent to each other
			new_student = set([student_name])
			self.db[grade] = old_roster | new_student
		elif grade not in keys: #if the student is entering a grade that doesn't already have any students in it
			self.db[grade] = {student_name}
		print "OK."
		return self.db
	
	def grade(self, grade):
		print "Which students are in grade " + str(grade) + "?"
		keys = self.db.keys() #creates a list of the dictionary keys, i.e. all of the grades with students in them
		if grade in keys: #IF a grade has students in it (the exact message returned depends on how many students in the grade)...
			if len(self.db[grade])==1:
				names = list(self.db[grade])
				print "We've only got " + names + " right now."
			elif len(self.db[grade])==2:
				names = list(self.db[grade])
				print "We've only got " + names[0] + " and " + names[1] + " right now."
			elif len(self.db[grade])>=3:
				names = list(self.db[grade])
				string = ""
				for i in range(0, len(names)):
					string = string + names[i] + ", "
				string = string + " and " + names[len(names)+1]
				print "We've got " + string + " right now."
			return self.db[grade]
		else: #IF a grade does not have students in it...
			print "There are no students in grade " + str(grade) + " right now."
			None
	
	def sort(self):
		print "Who all is enrolled in school right now?"
		keys = self.db.keys()
		for grade in keys: #This for loop sorts each grade
			student_list = self.db[grade]
			self.db[grade] = tuple(sorted(student_list))
		new_dictionary = {}
		for grade in keys: #This for loop sorts the grades in the dictionary so they are in ascending order
			new_dictionary[grade] = self.db[grade]
		for grade in range(1, max(max(keys) + 1, 9)): #This for loop runs through at least grades 1 through 8; however if there are any higher grades (e.g. grades 9 through 12) it will also include them as well
			if grade in keys: #If there are students in a particular grade, then the dictionary should have a key with that grade number. 
							  #This if statement prints out a slightly different message based on the number of students in the grade. 
				names = list(self.db[grade])
				string = ""
				if len(names)==1:
					print "\nGrade " + str(grade) + ": " + names[0]
				elif len(names)==2:
					string = names[0] + " and " + names[1]
					print "\nGrade " + str(grade) + ": " + string  
				elif len(names)>=3:
					for i in range(0, len(names)):
						string = string + names[i] + ", "
					string = string + " and " + names[-1]
					print "\nGrade " + str(grade) + ": " + string + "."
			elif grade not in keys: #What to do if there are no students in a grade.
				print "\nGrade " + str(grade) + ": None."
		return new_dictionary #returns the sorted database