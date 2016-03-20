
# coding: utf-8

# In[1]:

import pandas as pd, matplotlib.pyplot as plt, seaborn as sns
get_ipython().magic('matplotlib inline')

pixar_movies = pd.read_csv("PixarMovies.csv")
rows = pixar_movies.shape[0]
cols = pixar_movies.shape[1]

print(pixar_movies.head(rows))


# A printout of the rows and columns of the PixarMovies.csv dataset after reading it into the pixar_movies DataFrame object. The 'shape' function returns the dimensions of the DataFrame while passing in the total number of rows into head prints out each row.

# In[2]:

pixar_movies.dtypes


# Calling 'dtypes' on the DataFrame shows each of the columns' respective datatypes. 

# In[3]:

pixar_movies.describe()


# A 'description' of the dataset. For each numerical column we can see the mean, standard deviation, minimum value,25th percentile value, 50th percentile value, 75th percentile value, and maximum value.

# In[4]:

pixar_movies['Domestic %'] = pixar_movies['Domestic %'].str.rstrip('%').astype('float')
pixar_movies['International %'] = pixar_movies['International %'].str.rstrip('%').astype('float')
pixar_movies['IMDB Score'] = pixar_movies['IMDB Score']*10
filtered_pixar = pixar_movies.loc[0:13]



# Here the 'Domestic %' and 'International %' columns are converted into floats so that they may be compared. The 'IMDB Score' column is scaled up by 10 to bring its data onto a scale of 100.
# 
# filtered_pixar is the pixar_movies database with the last row dropped since the data for the last movie, 'Inside Out', wasn't reliably available at this time.

# In[11]:

pixar_movies.set_index('Movie',inplace=True)
filtered_pixar.set_index('Movie',inplace=True)


# Here both of the DataFrames are set with an index of the 'Movie' column. The inplace attribute is set to True so that the DataFrames are altered as is instead of returning a new DataFrame object.

# In[15]:

critics_reviews = pd.DataFrame(data=pixar_movies,columns=['RT Score','IMDB Score','Metacritic Score'])
critics_reviews.plot(kind='bar',rot=90,figsize=(13,5),legend='reverse')
plt.show()


# The three movie score columns are plotted to see how they comparably rate the films. 

# In[14]:

critics_reviews.plot(kind='box',figsize=(9,5))
plt.show()


# Here a box plot shows the distrubution of scores based on the review source. Rotten Tomatoes tends to give higher scores to Pixar movies while Metacritic's scores are across a wider range.

# In[15]:

revenue_proportions = pd.DataFrame(data=pixar_movies,columns=['Domestic %','International %'])
revenue_proportions.plot(kind='bar',stacked=True)
plt.show()


# A stacked bar graph shows the split between earning from domestic and international audiences. A quick look tells us that Ratatouille, Cars 2, and Monsters University had the highest percentage of their earnings internationally.

# In[19]:

prod_gross = pd.DataFrame(data=pixar_movies,columns=['Production Budget','Worldwide Gross'])
prod_gross.plot(rot=90)
plt.show()


# This simple line plot shows the relationship between production budget and the worldwide gross amount for each movie.

# In[22]:

oscars = pd.DataFrame(data=pixar_movies, columns=['Oscars Nominated','Oscars Won'])
oscars.plot(kind='bar')
plt.show()


# The bar graph here compares the number of Oscars a movie was nominated for to the number it actually won. WALL-E was nominated for six though won one while The Incredibles was nominated for four and ended up winning two.

# In[51]:

adg_correlate = pd.DataFrame(data=pixar_movies)
ac = sns.PairGrid(data=adg_correlate,x_vars=['Length','Year Released','RT Score','IMDB Score','Metacritic Score'],y_vars=['Adjusted Domestic Gross'],aspect=1.5,size=2)
ac = ac.map(plt.bar)


# This PairGrid was made using the Seaborn library while each of the previous graphs in this notebook used Pandas. Seaborn provides another api for drawing statistical graphics. This plot compares the film length, release year, and review scores to the adjusted domestic gross just to see if there's any correlation betwen them at all.
