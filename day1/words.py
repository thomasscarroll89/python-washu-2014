file = open('words.txt')

def has_no_e(word):
	return "e" not in word

def uses_only(word1, word2):
	for i in word:
		if not i in word2:
			return FALSE
	return TRUE

def uses_all(word1, word2):
	uses_only(word2, word1)

def is_abecedarian(word):
	word = word.lower()
	for i in range(0, len(word)-1):
		if word[i] <= word[i+1]:
			continue
		else:
			return FALSE
	return TRUE
				

				
for line in file:
  word = line.strip()
  print has_no_e(word)
  print word