import nltk

s = "This is a test sentence that is being used to test some text mining pre-processing. I am hoping that it would working and we will get along easily with this course. I am having fun! 232"

words = nltk.word_tokenize(s)

words=[word.lower() for word in words if word.isalpha()]

print(words)