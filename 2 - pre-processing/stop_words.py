import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

def remove_stop_words(string):
    stop_words = set(stopwords.words('english'))
    words = string.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    new_string = ' '.join(filtered_words)
    return new_string

# Example usage
input_string = "This is a test sentence that is being used to test some text mining pre-processing. I am hoping that it would working and we will get along easily with this course. I am having fun!"
result = remove_stop_words(input_string)
print("Original string:", input_string)
print("Modified string:", result)