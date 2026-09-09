import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('netflix_titles.csv')
print(df.head())
print(df['type'].value_counts())
df['type'].value_counts().plot(kind='bar')
plt.tight_layout()
plt.savefig('movies_vs_tvshows.png')
print('Chart saved.')
