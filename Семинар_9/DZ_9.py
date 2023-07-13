



import pandas as pd # подключение к библиотеке где pd это сокращение от pandas


df = pd.read_csv('sample_data/california_housing_train.csv') 
df.head(n=5)