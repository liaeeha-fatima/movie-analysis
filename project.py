import pandas as pd

# خواندن فایل CSV
df = pd.read_csv("movies.csv")

# مشاهده 5 ردیف اول
print(df.head())

print(df.info())

print(df.describe())

print(df['genre'].value_counts())

top5 = df.sort_values(by='imdb_rating', ascending=False).head(5)
print("Top 5 Movies by Rating:")
print(top5)



genre_avg = df.groupby('Genre')['Rating'].mean()
print("Avrage Rating by Genre:")
print(genre_avg)


genere_count = df['Genre'].value_counts()
print("Number of movies by Genre:")
print(genere_count)




import matplotlib.pyplot as plt

genre_avg.plot(kind='bar' , color='skyblue')
plt.title("Avrage Rating by Genre")
plt.xlabel("Genre")
plt.ylabel("Avrage Rateing")
plt.xticks(rotation=45)
plt.show()