import pandas as pd

# We create a Pandas Series that stores a grocery list
groceries = pd.Series(data = [30, 6, 'Yes', 'No'], index = ['eggs', 'apples', 'milk', 'bread'])

# We display the Groceries Pandas Series
groceries

fruits= pd.Series(data = [10, 6, 3,], index = ['apples', 'oranges', 'bananas'])

print(fruits)
