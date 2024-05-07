from apriori_python import apriori

itemSetList = [['milk', 'bread', 'butter'], ['milk', 'bread'], ['milk', 'butter'], ['bread', 'butter'], ['milk', 'bread', 'butter', 'eggs'], ['eggs', 'butter']]

freqItemSet, rules = apriori(itemSetList, minSup=0.5, minConf=0.5)
# print(freqItemSet)
print(rules)  
# [[{'beer'}, {'rice'}, 0.6666666666666666], [{'rice'}, {'beer'}, 1.0]]
# rules[0] --> rules[1], confidence = rules[2]