# Python3 code to remove whitespace
def remove(string):
	ns=""
	for i in string:
		if(not i.isspace()):
			ns+=i
	return ns 
# Driver Program
string = 'This is a test sentence that is being used to test some text mining pre-processing. I am hoping that it would working and we will get along easily with this course. I am having fun! 232'
print(remove(string))
