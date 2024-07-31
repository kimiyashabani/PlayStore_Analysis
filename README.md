# Play Store Data Analysis
This project consists of processing and analyzing a dataset of mobile applications from Google Play Store, leveraging various data cleaning and visualization techniques to derive insights. 

## Data Cleaning
- Deleting unnecessary columns
- Handling missing values
- Removing duplicates
## Identifying Highest Rated Applications
Identifying and isolating applications with the highest user ratings.

## Largest Applications 
The dataset is sorted to find the top five largest applications in file size.

## Data Visualization with Donut Charts
 ![App Screenshot](https://github.com/user-attachments/assets/1567e4f3-e196-485e-866b-66ff04556598)
Application content ratings are visualized using a donut chart to show the distribution of ratings.

## Numeric Type Conversion:

- The 'Installs' column, which contains commas, is cleaned and converted to numeric format.
- The 'Price' column, which contains dollar signs, is cleaned and converted to numeric format.
- Applications priced over $250 are filtered out to focus on realistic price ranges.

## Revenue Estimation:
The script calculates an estimated revenue for each application by multiplying the number of installs by the price.

## Bar Plot and Scatter Plots Visualization:

- Top Categories: The top 10 categories by number of applications are visualized.
  ![App Screenshot](https://github.com/user-attachments/assets/a4cf134e-60fe-420f-bc8e-b2031ff9346a)
- Category Popularity: The total number of installs per category is visualized.
  ![App Screenshot](https://github.com/user-attachments/assets/1a550555-bdc1-43f5-a7d7-e7afa0598afc)
- Category Concentration: A scatter plot is used to show the relationship between the number of applications in a category and the total installs, indicating market concentration.
  ![App Screenshot](https://github.com/user-attachments/assets/bf56ac53-1014-4920-a8c7-4ac53bf882a8)
## Extracting Nested Data:
The 'Genres' column, which contains multiple genres separated by semicolons, is split and the top genres are visualized.

## Analyzing Free vs Paid Apps:
A grouped bar chart is used to compare the number of free and paid applications across different categories.

## Free vs Paid Apps Downloads Analysis:
A box plot is used to analyze the distribution of downloads between free and paid applications.

## Free vs Paid Apps Downloads Analysis:
A box plot is used to analyze the distribution of downloads between free and paid applications.


