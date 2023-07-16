#!/usr/bin/env python
# coding: utf-8

# * # Parental Leave Policies

# # Data Understanding

# #### Crowdsourced parental leave data from 1,601 companies across different industries, including paid/unpaid maternity and paternity leave weeks.
# 
# * Company - Company name
# * Industry - Company Industry & sub-industry (Industry: Sub-industry)
# * Paid Maternity Leave-  Paid weeks off from work for mothers after the birth of their child
# * Unpaid Maternity Leave-  Unpaid weeks off from work for mothers after the birth of their child
# * Paid Paternity Leave-  Paid weeks off from work for fathers after the birth of their child
# * Unpaid Paternity Leave-  Unpaid weeks off from work for fathers after the birth of their child
# 
# NOTE: This is user-reported data. Where users report conflicting information, consensus numbers (if any) or the median are shown. "N/A" means no information has been reported.
# 
# 

# <img src = "https://res.cloudinary.com/people-matters/image/upload/q_auto,f_auto/v1632456323/1632456322.jpg">

# # Importing Liebraries

# In[448]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[449]:


data = pd.read_csv("parental_leave.csv", encoding = "latin-1")  # importing the data from the source


# ******

# In[450]:


data.head()  # printing head/top 5 rows for overview of the data.


# In[451]:


data = data.iloc[:,0:6]             #fetching the required columns for the analysis.


# In[452]:


data.columns                        # fetching the names of the columns


# In[453]:


data.isnull().sum()                 # Checking weather the null values are present in the dataset.


# In[454]:


data.info()


# In[455]:


# creating a for loop to fetch the indexes of the records which has missing industry
l = []
for i in data[data["Industry"].isnull()].index:  value
    l.append(i)

data.drop(index = l, axis = 1, inplace = True)


# In[456]:


data.duplicated().sum()


# In[457]:


data.fillna(0, inplace =True)


# In[458]:


data


# ******

# ### 1. Which companies offer the most paid parental leave weeks?

# In[459]:


# performed operations to fetch the company names which offers most parental leave.
companies = data[["Company", "Paid Maternity Leave", "Paid Paternity Leave"]]
companies["Paid Parental Leave"] = companies["Paid Maternity Leave"] + companies["Paid Paternity Leave"]
companies = companies.sort_values(by = "Paid Parental Leave", ascending = False).head(10)
companies.drop(["Paid Parental Leave"], axis = 1, inplace =True)
companies


# #### companies offer the most paid parental leave weeks are as follows - 
# * Grant Thornton 
# * LAC-Group
# * Flatiron Health
# * Cloudworkers
# * LeverX
# * Rangle.io
# * Washburn Center For Children
# * Salesforce
# * JHC Systems
# * Dynatrace
# 

# In[631]:


from matplotlib.pyplot import figure
figure(figsize = (10,4))
plt.plot(companies['Company'], companies['Paid Paternity Leave'], '-b', label = 'Paid Paternity Leave')
plt.bar(companies['Company'], companies['Paid Maternity Leave'], color = 'orange', label = 'Paid Maternity Leave', width = 0.5)
plt.xlabel("Companies")
plt.ylabel("Leaves in Weeks")
plt.xticks(rotation = 90)
plt.title("Most paid leave offered by companies")
plt.legend()
plt.show()


# ******

# ### 2. Is maternity leave typically longer than paternity leave?

# In[461]:


data["Total Maternity Leave"] = data["Paid Maternity Leave"] + data["Unpaid Maternity Leave"]
data["Total Paternity Leave"] = data["Paid Paternity Leave"] + data["Unpaid Paternity Leave"]


# In[649]:


figure(figsize = (10,3))
sns.scatterplot(data = data, x = "Paid Paternity Leave" ,  y = "Paid Maternity Leave", color = 'purple' )
plt.show()


# #### As we can see in the above scatter plot, most of the company is providing Maternity Leave and does not offers Paternity leave or while some of the companies provide less paternity leave than maternity leave.
# #### So, We can say Maternity Leave is longer than Paternity Leave.

# ******

# ### 3. What is the distribution of parental leave weeks offered?

# In[463]:


fig, axes = plt.subplots(1, 2, figsize=(15, 4), sharey = True)
sns.distplot(ax = axes[0], a =data["Total Maternity Leave"])
axes[0].set_title("Maternity Leave")

sns.distplot(ax = axes[1], a = data["Total Paternity Leave"], color = 'orange')
axes[1].set_title("Paternity Leave")


# In[464]:


figure(figsize = (10,4))
sns.distplot(data["Total Maternity Leave"])
sns.distplot(data["Total Paternity Leave"], color = 'orange')


# In[638]:


print("Average Maternity Leave: ",data["Total Maternity Leave"].mean().round(1),"and ","Std of Maternity Leave: ",data["Total Maternity Leave"].std().round(1) )
print("Average Paternity Leave: ",data["Total Paternity Leave"].mean().round(1),"and ","Std of Maternity Leave: ",data["Total Paternity Leave"].std().round(1) )


# * #### Distribution of both Maternity and Paternity Leave is almost seems like normal distribution with very less skewed to the right. 
# * #### std for maternity leave is greater than paternity leave. and spread of the data in maternity leave is more and wide than that of paternity leave as more than 50% data in paternity leave is very close to mean. And in maternity data the data is spreaded over some std value.

# ******

# ### 4. Are there noticeable differences between industries?

# In[589]:


ind = data[['Industry', 'Paid Maternity Leave', 'Unpaid Maternity Leave', 'Paid Paternity Leave', 'Unpaid Paternity Leave']]
ind["Industry"] = ind["Industry"].apply(lambda x: x.split(":"))
ind["Industry"] = ind["Industry"].apply(lambda x: x[0])
ind


# In[623]:


ind = ind.groupby(by = "Industry").mean().round(1)


# In[640]:


figure(figsize = (10,4))
plt.plot(ind.index, ind['Paid Maternity Leave'], '-b', label = 'Paid Maternity Leave')
plt.bar(ind.index, ind['Unpaid Maternity Leave'], color = 'orange', label = 'Unpaid Maternity Leave', width = 0.5)
plt.plot(ind.index, ind['Paid Paternity Leave'], '-g', label = 'Paid Paternity Leave')
plt.bar(ind.index, ind['Unpaid Paternity Leave'], color = 'red', label = 'Unpaid Paternity Leave', width = 0.5)
plt.xlabel("Industry")
plt.ylabel("Leaves in Weeks")
plt.xticks(rotation = 90)
#plt.title("Most paid leave offered by companies")
plt.legend()
plt.show()


# * #### In every Industry Paid Maternity leave is longer than Paid Paternity leave.
# * #### Also Unpaid Maternity Leave is longer than Unpaid Paternity Leave.
# * #### Only Pharmacies and Drug Stores offers equal Unpaid Maternity as well as Paternity Leave.
# * #### Printing Industry offers same weeks of Paid Maternity and Paternity Leave. Also it offers highest no. of unpaid week leave

# ******
