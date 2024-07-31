import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Showing numeric output in 2 decimal places
pd.options.display.float_format = '{:,.2f}'.format

# TODO 1: LOAD THE DATASET

df_apps = pd.read_csv('apps.csv')

# TODO 2: DATA CLEANING
# Deleting the column "Last Updated" and "Android Ver" because we do not use these columns :
df_apps.drop(columns=['Last_Updated', 'Android_Ver'], axis=1 , inplace=True)
# Finding the nan values and drop them :
nan_rows = df_apps[df_apps.Rating.isna()]
clean_df_apps = df_apps.dropna()
# Find and remove duplicates
duplicated_rows = clean_df_apps[clean_df_apps.duplicated()]
#Example: we check how many duplicates we have for instagram:
# duplicated_instagram = clean_df_apps[clean_df_apps.App == 'Instagram']
# print(duplicated_instagram)
clean_df_apps = clean_df_apps.drop_duplicates(subset=['App','Type','Price'])

# TODO 3: FIND HIGHEST RATED APPLICATIONS
highest_rated = clean_df_apps.Rating.max()
max_rated_apps = clean_df_apps[clean_df_apps.Rating == highest_rated]

# TODO 4: FIND 5 LARGEST APPLICATIONS IN TERMS OF SIZE (MBs)
#print(clean_df_apps.sort_values(by='Size_MBs', ascending=False))

# TODO 5: DONUT CHARTS DATA VISUALIZATION
# ratings = clean_df_apps.Content_Rating.value_counts()
# print(ratings)
#
# figure = px.pie(labels=ratings.index,
#                 values=ratings.values,
#                 title="Content Rating",
#                 names=ratings.index,
#                 hole=0.6)
# figure.update_traces(textposition='outside', textinfo='percent+label')
# figure.show()

# TODO 6: Numeric type conversion
clean_df_apps.Installs.describe()
# we see we have ',' sign and '$' sign ,and we need to remove them
clean_df_apps.Installs = clean_df_apps.Installs.astype(str).str.replace(',', '')
clean_df_apps.Installs = pd.to_numeric(clean_df_apps.Installs)

clean_df_apps.Price = clean_df_apps.Price.astype(str).str.replace('$', '')
clean_df_apps.Price = pd.to_numeric(clean_df_apps.Price)

# All prices for the applications should be fewer than 250$:
clean_df_apps = clean_df_apps[clean_df_apps.Price <= 250]

# TODO 7: REVENUE ESTIMATION
clean_df_apps['Revenue_Estimate'] = clean_df_apps.Installs.mul(clean_df_apps.Price)

# TODO 8: BAR PLOT AND SCATTER PLOTS VISUALIZATION
top_10_cat = clean_df_apps.Category.value_counts()[:10]
# bar = px.bar(x=top_10_cat.index, y=top_10_cat.values, title='Top 10 Categories on Google Play Store')
# bar.show()

category_installs = clean_df_apps.groupby('Category').agg({'Installs': pd.Series.sum})
# category_installs.sort_values('Installs', ascending=True, inplace=True)
# h_bar = px.bar(x = category_installs.Installs,
#                y = category_installs.index,
#                orientation='h',
#                title='Category Popularity')
#
# h_bar.update_layout(xaxis_title='Number of Downloads', yaxis_title='Category')
# h_bar.show()

category_number = clean_df_apps.groupby('Category').agg({'App': pd.Series.count})
merged_df = pd.merge(category_installs, category_number, on='Category', how='inner')
# scatter = px.scatter(merged_df, # data
#                     x='App', # column name
#                     y='Installs',
#                     title='Category Concentration',
#                     size='App',
#                     hover_name=merged_df.index,
#                     color='Installs')
#
# scatter.update_layout(xaxis_title="Number of Apps (Lower=More Concentrated)",
#                       yaxis_title="Installs",
#                       yaxis=dict(type='log'))
#
# scatter.show()

# TODO 9 : EXTRACTING NESTED DATA
stack = clean_df_apps.Genres.str.split(';', expand=True).stack()
num_genres = stack.value_counts()
# bar = px.bar(x = num_genres.index[:15], # index = category name
#              y = num_genres.values[:15], # count
#              title='Top Genres',
#              hover_name=num_genres.index[:15],
#              color=num_genres.values[:15],
#              color_continuous_scale='Agsunset')
#
# bar.update_layout(xaxis_title='Genre',
# yaxis_title='Number of Apps',
# coloraxis_showscale=False)
#
# bar.show()

# TODO 10: ANALYZING FREE VS PAID APPS
free_vs_paid = clean_df_apps.groupby(["Category","Type"], as_index=False).agg({"App": pd.Series.count})
g_bar = px.bar(free_vs_paid,
               x='Category',
               y='App',
               title='Free vs Paid Apps by Category',
               color='Type',
               barmode='group')

g_bar.update_layout(xaxis_title='Category',
                    yaxis_title='Number of Apps',
                    xaxis={'categoryorder': 'total descending'},
                    yaxis=dict(type='log'))

g_bar.show()

# TODO 11: FREE VS PAID APPS DOWNLOADS ANALYSIS
# box = px.box(clean_df_apps,
#              y='Installs',
#              x='Type',
#              color='Type',
#              notched=True,
#              points='all',
#              title='How Many Downloads are Paid Apps Giving Up?')
#
# box.update_layout(yaxis=dict(type='log'))
#
# box.show()

# TODO 12: REVENUE BY APP CATEGORY
paid_apps = clean_df_apps[clean_df_apps.Type == 'Paid']
# box = px.box(paid_apps,
#              x='Category',
#              y='Revenue_Estimate',
#              title='How Much Can Paid Apps Earn?')
#
# box.update_layout(xaxis_title='Category',
#                   yaxis_title='Paid App Ballpark Revenue',
#                   xaxis={'categoryorder': 'min ascending'},
#                   yaxis=dict(type='log'))
#
# box.show()
