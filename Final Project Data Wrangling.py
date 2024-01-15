#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Import the dataset using Pandas from url:https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv


# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import requests


# In[2]:


corona_dataset = pd.read_csv('https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv')
corona_dataset.head(10)
     


# In[ ]:


#2 .High Level of Understanding:
#a) Find No. of Rows & columns in the dataset


# In[3]:


corona_dataset.shape 


# In[ ]:


# b) Datatypes of Coloumns


# In[5]:


corona_dataset.dtypes


# In[ ]:


# c) Info & Describe of Data in Dataframe


# In[6]:


corona_dataset.info()


# In[4]:


corona_dataset.describe()


# In[ ]:


#3. Low Level Data Understanding :
#a)Find count of unique values in location column


# In[7]:


corona_dataset['location'].unique()


# In[ ]:


# b. Find which continent has maximum frequency using values
# counts


# In[8]:


corona_dataset['continent'].value_counts().idxmax()


# In[ ]:


# c. Find maximum & mean value in 'total_cases'


# In[9]:


corona_dataset['total_cases'].max()


# In[10]:


corona_dataset['total_cases'].mean()


# In[ ]:


#  d. Find 25%,50% & 75% quartile value in 'total_deaths'.


# In[11]:


quartiles = corona_dataset['total_deaths'].quantile([0.25, 0.5, 0.75])
quartiles


# In[ ]:


# e. Find which continent has maximum 'human_development_index'.


# In[12]:


corona_dataset.loc[corona_dataset['human_development_index'].idxmax(), 'continent']


# In[13]:


#  f. Find which continent has minimum 'gdp_per_capita'.


# In[14]:


corona_dataset.loc[corona_dataset['gdp_per_capita'].idxmin(), 'continent']


# In[ ]:


# 4. Filter the dataframe with only this columns
# ['continent','location','date','total_cases','total_deaths',
# 'gdp_per_capita','human_development_index'] and update the data frame.


# In[15]:


corona_dataset[['continent', 'location', 'date', 'total_cases', 'total_deaths', 'gdp_per_capita', 'human_development_index']]


# In[ ]:


5. Data Cleaning
#a. Remove all duplicates observations


# In[16]:


corona_dataset.drop_duplicates()


# In[ ]:


#  b. Find missing values in all columns


# In[17]:


missing_values = corona_dataset.isnull().sum()
missing_values


# In[ ]:


#  c. Remove all observations where continent column value is missing
# Tip : using subset parameter in dropna


# In[18]:


corona_dataset.dropna(subset=['continent'])


# In[ ]:


# d. Fill all missing values with 0


# In[19]:


corona_dataset.fillna(0)


# In[ ]:


6. Date time format :
#a. Convert date column in datetime format using pandas.to_datetime


# In[20]:


corona_dataset['date'] = pd.to_datetime(corona_dataset['date'])
corona_dataset


# In[ ]:


# b. Create new column month after extracting month data from date column.


# In[21]:


corona_dataset['month'] = corona_dataset['date'].dt.month
corona_dataset
     


# In[ ]:


#7. Data Aggregation:
a. Find max value in all columns using groupby function on 'continent' column b. Store the result in a new dataframe named 'df_groupby'.


# In[22]:


corona_dataset.groupby('continent').max()


# In[23]:


corona_dataset_groupby = corona_dataset.groupby('continent').max().reset_index()
corona_dataset


# In[ ]:


#8.Feature Engineering :
a. Create a new feature 'total_deaths_to_total_cases' by ratio of 'total_deaths' column to 'total_cases'


# In[24]:


corona_dataset['total_deaths_to_total_cases'] = corona_dataset['total_deaths'] / corona_dataset['total_cases']
corona_dataset['total_deaths_to_total_cases']


# In[ ]:


#9. Data Visualization :
a. Perform Univariate analysis on 'gdp_per_capita' column by plotting histogram using seaborn dist plot


# In[25]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[26]:


sns.displot(corona_dataset['gdp_per_capita'])
plt.show()
     


# In[ ]:


# b. Plot a scatter plot of 'total_cases' & 'gdp_per_capita'


# In[27]:


plt.scatter(corona_dataset['gdp_per_capita'], corona_dataset['total_cases'])
plt.xlabel('GDP per Capita')
plt.ylabel('Total Cases')
plt.title('Scatter Plot: Total Cases vs. GDP per Capita')
plt.show()


# In[ ]:


#c. Plot Pairplot on df_groupby dataset.


# In[ ]:


sns.pairplot(corona_dataset_groupby)
plt.show()


# In[ ]:


#d. Plot a bar plot of 'continent' column with 'total_cases' . Tip : using kind='bar' in seaborn catplot


# In[ ]:


plt.figure(figsize=(10, 6))
sns.barplot(x='continent', y='total_cases', data=corona_dataset)
plt.xlabel('Continent')
plt.ylabel('Total Cases')
plt.title('Bar Plot: Total Cases by Continent')
plt.show()


# In[ ]:


# 10.Save the df_groupby dataframe in your local drive using pandas.to_csv function .



# In[ ]:


corona_dataset.to_csv('Corona_Dataset.csv', index=False)

