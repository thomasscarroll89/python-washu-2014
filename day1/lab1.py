def binarify(num): 
  """convert positive integer to base 2"""
  if num<=0: return '0'
  digits = []
  for i in range(0,100): 
	if num/(2**i) > 1:
		continue
	else: 
		digits.append('1')
		num = num - 2**i
		length = i
		break
  for j in range((length-1),-1, -1):
	if num/(2**j) >= 1:
		digits.append('1')
		num = num - (2**j)
	else:
		digits.append('0')
  return ''.join(digits)
  
print binarify(17)  

def int_to_base(num, base):
  """convert positive integer to a string in any base"""
  if num<=0:  return '0' 
  digits = []
  for i in range(0,100): 
	if num/float((base**i)) > 1:
		continue
	else: 
		digits.append(str(num//(base**(i-1))))
		num = num - (num//(base**(i-1)))*(base**(i-1))
		length = i
		break
  for j in range((length-2),-1, -1):
		digits.append(str(num//(base**j)))
		num = num - (num//(base**(j)))*(base**j)
  return ''.join(digits)

print int_to_base(918, 10)
print int_to_base(28, 3)
print int_to_base(30, 4)
print int_to_base(50, 7)

 
def base_to_int(string, base):
  """take a string-formatted number and its base and return the base-10 integer"""
  if string=="0" or base <= 0 : return 0 
  result = 0 
  string = list(string)
  result = 0
  for i in range(0, len(string) + 1):
	result = result + string[i]*(base**len(string)-i)
  return result 
  
base_to_int(101, 7)

def flexibase_add(str1, str2, base1, base2):
  """add two numbers of different bases and return the sum"""
  result = int_to_base(tmp, base1)
  return result 

def flexibase_multiply(str1, str2, base1, base2):
  """multiply two numbers of different bases and return the product"""
  result = int_to_base(tmp, base1)
  return result 

def romanify(num):
  """given an integer, return the Roman numeral version"""
  result = ""
  return result