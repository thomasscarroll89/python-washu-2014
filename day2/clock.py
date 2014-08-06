class Clock():
	def __init__(self, hours, minutes=0):
		self.hours = hours
		self.minutes = minutes
		self.total_minutes = int(self.hours)*60 + int(self.minutes)
	
	@classmethod
	def at(cls, hours, minutes=00):	
		return cls(hours, minutes)
	
	def __add__(self, other):
		x = int(self.hours)*60 + int(self.minutes)
		total_minutes = x + other
		final_hours = total_minutes//60
		final_minutes = total_minutes%60
		return Clock(hours=final_hours, minutes=final_minutes)
	
	def __sub__(self, other):
		x = int(self.hours)*60 + int(self.minutes)
		total_minutes = x - other
		final_hours = total_minutes//60
		final_minutes = total_minutes%60
		return Clock(hours=final_hours, minutes=final_minutes)
	
	def __str__(self):
		total_minutes = int(self.hours)*60 + int(self.minutes)
		final_hours = total_minutes//60
		if final_hours < 10:
			final_hours = "0" + str(final_hours)
		final_minutes = total_minutes%60
		if final_minutes < 10:
			final_minutes = "0" + str(final_minutes)
		while int(final_hours) >= 24:
			final_hours = int(final_hours) - 24
		return str(final_hours) + ":" + str(final_minutes)
		

print Clock.at(8).__str__()
print Clock.at(9).__str__()
print Clock.at(11, 9).__str__()
clock = Clock.at(10) + 3
print clock.__str__()
print Clock.at(25).__str__()
