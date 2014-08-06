from speak import *
import unittest

class SpeakTest(unittest.TestCase):
	
	def test_speak_question(self):
		self.assertEqual("Sure.", speak("Are you hungry?"))
		self.assertEqual("Woah, chill out!", speak("YOU IDIOT!"))
		self.assertEqual("Fine. Be that way!", speak(""))
		self.assertEqual("Whatever.", speak("Pigs can't fly"))
		self.assertEqual("Woah, chill out! Sure.", speak("ARE YOU AN IDIOT?"))
		self.assertEqual("Sure.", speak("?"))
		
if __name__ == '__main__':
  unittest.main() 