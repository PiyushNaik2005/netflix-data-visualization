import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\piyus\OneDrive\Documents\Study_material\matplot project\netflix-data-analysis\netflix_titles.csv')

print(df.head)

df = df.dropna(subset = ['type','release_year','rating','country','duration'])

type_counts = df['type'].value_counts()
plt.figure(figsize = (6,4))
plt.bar(type_counts.index, type_counts.values, color = ['skyblue','orange']) #-------------------------------------
plt.title("Number of Movies Vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")

plt.tight_layout()
plt.savefig("Movies_vs_TVShows.png")

plt.show()

rating_counts = df["rating"].value_counts()
top_n = 6
top_ratings = rating_counts.head(top_n)
other_total = rating_counts.iloc[top_n:].sum()

if other_total > 0:
    top_ratings = pd.concat([top_ratings, pd.Series({'Other': other_total})])

plt.figure(figsize=(8,6))
plt.pie(
    top_ratings,
    labels=top_ratings.index,
    autopct='%1.1f%%',
    startangle=90,
    pctdistance=0.8,          # pushes % labels inward, away from edge
    labeldistance=1.05        # pushes category labels slightly outward
)
plt.title("Percent of Content Ratings")
plt.tight_layout()
plt.savefig("Content_rating_pie_clean.png")
plt.show()  



movies_df = df[df['type'] == "Movie"].copy()    #----------------------------------
movies_df['duration_int'] = movies_df['duration'].str.replace('min','').astype(int)  #----------------------------------

plt.figure(figsize = (8,6))
plt.hist(movies_df['duration_int'], bins= 30, color='purple', edgecolor = 'black')
plt.title("Distribution of Movie Duration")
plt.xlabel("Duration (Minutes)")
plt.ylabel("Number of Movies")

plt.tight_layout()
plt.savefig("Movie_Duration_Hist.png")

plt.show()



release_count =df['release_year'].value_counts().sort_index()
plt.figure(figsize = (10,6))
plt.scatter(release_count.index, release_count.values, color = 'red')
plt.title("Release Year VS Number of Shows")
plt.xlabel("Release Year")
plt.ylabel("Number of Shows")

plt.tight_layout()
plt.savefig("Release_Year.png")
plt.show()



country_counts = df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_counts.index, country_counts.values, color = 'green')
plt.title("Top 10 Countries by number ")
plt.xlabel("Number of Shows")
plt.ylabel("Country")

plt.tight_layout()
plt.savefig("Top_10_Countries.png")
plt.show()


content_by_year = df.groupby(['release_year','type']).size().unstack().fillna(0)
fig, ax = plt.subplots(1,2, figsize = (12,5))

ax[0].plot(content_by_year.index,content_by_year['Movie'],color = 'pink')
ax[0].set_title('Movies released per Year')
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Number of Movies")



ax[1].plot(content_by_year.index,content_by_year['TV Show'],color = 'blue')
ax[1].set_title('TV Shows released per Year')
ax[1].set_xlabel("Year")
ax[1].set_ylabel("Number of Shows")

fig.suptitle("Comparison of Movies and TV Shows Released Over Years")
plt.tight_layout()
plt.savefig("Movies_TVShows_Comparison.png")
plt.show()