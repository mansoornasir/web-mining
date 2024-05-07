# import the existing word and sentence tokenizing 
# libraries 
from nltk.tokenize import sent_tokenize, word_tokenize 

text = "This is a test sentence that is being used to test some text mining pre-processing. I am hoping that it would working and we will get along easily with this course. I am having fun!"

print(sent_tokenize(text)) 
print(word_tokenize(text))
