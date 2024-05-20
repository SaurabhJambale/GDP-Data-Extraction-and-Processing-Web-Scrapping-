import numpy as np
import pandas as pd

import warnings

warnings.filterwarnings('ignore')

#Extracting data from below url
url="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

# Extract gdp dataframe 
dfs_list= pd.read_html(url, attrs =({'class':'wikitable sortable static-row-numbers plainrowheaders srn-white-background'}))

df=dfs_list[0]




# Replace the column headers with column numbers
df.columns = range(df.shape[1])

# Retain columns with index 0 and 2 (name of country and value of GDP quoted by IMF)
df=df[[0,2]]


# Retain the Rows with index 1 to 10, indicating the top 10 economies of the world.
df=df.iloc[1:11,:]


# Assign column names as "Country" and "GDP (Million USD)"
df.columns=["Country","GDP (Million USD)"]



# Change the data type of the 'GDP (Million USD)' column to integer.
df[['GDP (Million USD)']]=df[['GDP (Million USD)']].astype(int)

# Convert the GDP value in Million USD to Billion USD
df[['GDP (Million USD)']]=df[['GDP (Million USD)']]/1000


# Round the values of 'GDP (Million USD)' to 2 decimal places.
df[['GDP (Million USD)']]=np.round(df[['GDP (Million USD)']],2)

# Rename the column header from 'GDP (Million USD)' to 'GDP (Billion USD)'
df.rename(columns={'GDP (Million USD)':'GDP (Billion USD)'},inplace=True)

# Print processed dataframe
print(df)

# Save processed dataframe to excel file
df.to_excel('Top 10 countries by GDP.xlsx',sheet_name='sheet1')
