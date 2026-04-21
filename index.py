import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('/content/yourfile.csv')
df.head()
df.info()
df.describe()
highest_votes = df[df['Votes'] == df['Votes'].max()]
highest_votes
sns.barplot(x='Genre', y='Votes', data=df)
plt.xticks(rotation=90)
plt.show()