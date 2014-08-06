from lab3 import *
import unittest

class ShoutTest(unittest.TestCase):
	
	def test_shout_one(self):
		self.assertEqual("HELLO!", shout("hello"))

	def test_shout_two(self):
		self.assertEqual("HI! HOW ARE YOU DOING?!", shout("Hi! How are you doing?")) #Replaces a question mark with an exclamation mark; then adds a second excalamation mark at the end.
	
	def test_shout_three(self):
		self.assertEqual("HELLO!", shout("hello.")) #Is not replacing the period with an exclamation mark; this is because the string in the code has an extra space after it
	
	def test_two_sentences(self):
		self.assertEqual("MY NAME IS DALSTON! I LIKE CHEESE!", shout("My name is Dalston. I like cheese."))
	
	def test_many_questions(self):
		self.assertEqual("WHO ARE YOU?! WHAT ARE YOU DOING HERE?! DO YOU LIKE CHEESE?!", shout("Who are you? What are you doing here? Do you like cheese?"))
		
	#def test_abbreviations(self):
	#	self.assertEqual("D.R. WHO?!", shout("D.r. Who?"))
	
	def test_reverse_one_word(self):
		self.assertEqual("olleh", reverse("hello"))
		
	def test_space(self):
		self.assertEqual(" ecaps", reverse("space "))
	
	def test_two_words(self):
		self.assertEqual("sdrow owT", reverse("Two words"))
		
	#Next: reverse word order
	def test_one_sentence(self):
		self.assertEqual(".World Hello", reversewords("Hello World."))
	
	def test_multiple_sentences(self):
		self.assertEqual(".world Hello .today busy very I'm .chocolate like I ", reversewords("Hello world. I'm very busy today. I like chocolate."))
	
if __name__ == '__main__':
  unittest.main() 