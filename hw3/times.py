from timeit import Timer
import matplotlib.pyplot as plt

#Next, create a dictionary where the keys are the length of the list input for the selection sort, and the values are the time it takes to perform that sort 100 times.
time_selection ={} #Create empty dictionary
for i in range(1, 251):
	string = "from sorting import selection; import numpy; import random; data=list(numpy.random.normal(size=" + str(i) + "))" #create a string that simply changes the size of our list
	t = Timer("selection(list=data)", string) #run the timer function
	time_selection[i] = t.timeit(number=100) #extract the time it takes to run the selection sort
print time_selection

#Next do the same for the merge sort
time_merge = {}
for i in range(1, 251):
	string = "from sorting import merge_sort; import numpy; import random; data=list(numpy.random.normal(size=" + str(i) + "))"
	t = Timer("merge_sort(list=data)", string)
	time_merge[i] = t.timeit(number=100)
print time_merge

#Plot the outcome
plt.plot(time_selection.values(), label="Selection Sort")
plt.plot(time_merge.values(), label="Merge Sort")
plt.ylabel('Time')
plt.xlabel('List Size')
plt.legend(loc="upper left")
plt.show()
