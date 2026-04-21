import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("IMDB Dataset.csv")
print(df.head())
print(df.columns)
print(df.info())
print(df.describe())
highest_votes = df[df['Votes'] == df['Votes'].max()]
print(highest_votes)
sns.barplot(x='Genre', y='Votes', data=df)
plt.xticks(rotation=90)
plt.show()