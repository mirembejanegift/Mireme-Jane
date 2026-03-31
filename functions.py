
'''


'''

# we created a dynamic function and named it tests.
def tests(test1, test2):
	# here if the test1 is equal to test2 
	if test1 == test2:
		# python should return test1
		return test1
	else:
		# if the test1 and test2 are different python should return test2 
		return test2
# ask the user to enter marks for both tests
# int is to convert the the input in to whole numbers
test1 = int(input('Please enter Marks for test one: '))
test2 = int(input('Please enter Marks for test two: '))


'''


'''
# we created a dynamic function and named it courseWrk
def courseWrk(cswork):
	# we are invoking the tests function
	testsMark = tests(test1,test2)
	# we add cswork + testsMarks then divide by 2
	avgtestsCswork = (cswork + testsMark)/2
	#to get the finial score we get the average and calculate 40% of it
	fnltestsCswork = avgtestsCswork * (40/100)
	# print the final test
	print('..............................')
	# print is going to make python show on screen
	print('your final coursework marks is: ', fnltestsCswork)
	print('..............................')
# ask the user to input coursemarks
# int converts input to whole numbers
cswork = int(input('Please enter your course work Marks: '))
#  this is calling the function CourseWrk()
courseWrk(cswork)

