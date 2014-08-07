def Towers_of_Hanoi(start=None, goal=None, available=None):
	if start == None:
		start = []
	if goal == None:
		goal = []
	if available == None:
		available = []
	goal.insert(0, start.pop(0))
	if start == []:
		if (goal==[] or available==[]):
			print goal
			return "Congratulations! You won the game! You're free!"
		return Towers_of_Hanoi(start=available, goal=goal, available=start)
	if start != []:
		return Towers_of_Hanoi(start=start, goal=available, available=goal)	
	
#print Towers_of_Hanoi(start=[1])
print Towers_of_Hanoi(start=[1, 2])
print Towers_of_Hanoi(start=[1, 2, 3])
print Towers_of_Hanoi(start=[1, 2, 3, 4])