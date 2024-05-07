from mlxtend.frequent_patterns import fpgrowth
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd

# Create example dataset
dataset = [['milk', 'bread', 'butter'], ['milk', 'bread'], ['milk', 'butter'], ['bread', 'butter'], ['milk', 'bread', 'butter', 'eggs'], ['eggs', 'butter']]

# create transcation encoder and transform data
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

#generate frequent itemsets
frequent_itemsets = fpgrowth(df, min_support=0.05, use_colnames=True)

# sort frequent itemsets by support
frequent_itemsets = frequent_itemsets.sort_values(by='support', ascending=False)

print(frequent_itemsets.head(10))
