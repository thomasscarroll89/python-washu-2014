from math import floor #Used for rounding down (see merge_sort function)
from math import ceil #Used for rounding up (see merge_sort function)

def selection(list, k=0):
	for k in range(0, len(list)-1): #We don't need to run this for loop when k is the last element of the list, since by then the list will already be sorted
		first_element = list[k] #create an object that records the value of the first element that we are comparing to everything else in the list
		minimum_index = k #set the minimum_index to k, meaning k is (for now) the index of list that contains the lowest value
		for index in range(k+1, len(list)): #compare k^th element to every other element after it in list
			if list[index] < list[k]: #If any other element in list is smaller than k, reset minimum_index to be the new element's index number
				minimum_index = index
		minimum = list[minimum_index] #extract the value of the smaller element
		if minimum < first_element:
			list[k] = minimum #Switch the k^th element with the smaller element 
			list[minimum_index] = first_element	
	return list

def merge_sort(list):
	if len(list) <= 1:
		return list
	left = list[:len(list)/2]  #Python somehow automatically knows that, even though len(list)/2 is an integer (rounded down), that when we write the colon before
	right = list[len(list)/2:] #we want the first half up to that integer, and when the colon comes after we want the integer + 1. So this still works even for lists of odd length. 
	left = merge_sort(left) #recursive part
	right = merge_sort(right) #recursive
	i = 0; j = 0
	merged = [] #create empty list
	while len(merged) < (len(left) + len(right)):
		if (i >= len(left)):		 #This and the first elif statement are designed to catch cases where we've already gone through every element of either right or left.
			merged.append(right[j])	 #It basically just adds every remaining element of the right/left list onto the merged object in the original order. 
			j += 1					 #This way we avoid indexing problems that would otherwise arise whenever we finished one of the lists before the other. 
		elif (j >= len(right)):
			merged.append(left[i])
			i +=1
		elif (right[j] <= left[i]): #Next two elif statements kick in if the previous few lines did not run; basically just switch the smaller values with earlier values
			merged.append(right[j]) #when applicable, and then increment i/j
			j += 1
		elif left[i] < right[j]:
			merged.append(left[i])
			i += 1
	return merged	