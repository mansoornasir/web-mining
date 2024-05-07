from sklearn.feature_extraction.text import TfidfVectorizer

docA = "It was the best of times,"
docB = "it was the worst of times," 
docC = "it was the age of wisdom," 
docD = "it was the age of foolishness," 

tfidf = TfidfVectorizer()

response = tfidf.fit_transform([docA, docB, docC, docD])

feature_names = tfidf.get_feature_names_out()
for col in response.nonzero()[1]:
    print (feature_names[col], ' - ', response[0, col])