def speak(message):
	if ("?" in message) and (message.upper() == message) and message != "?":
		return "Woah, chill out! Sure."
		
	if "?" in message:
		return "Sure."

	elif message == "":
		return "Fine. Be that way!"

	elif message.upper() == message:
		return "Woah, chill out!"
	
	else:
		return "Whatever."	