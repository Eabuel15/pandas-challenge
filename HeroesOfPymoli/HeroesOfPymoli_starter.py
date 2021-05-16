#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[182]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()


# ## Player Count

# * Display the total number of players
# 

# In[183]:


total_player_count = len(purchase_data["SN"].value_counts())
player_count_df = pd.DataFrame({"Total Players" : [total_player_count]})
player_count_df


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[184]:


unique_items_count = len(purchase_data["Item Name"].value_counts())
avg_price = purchase_data["Price"].mean()
purchases_amt = purchase_data["Purchase ID"].count()
total_revenue = sum(purchase_data["Price"])
purchasing_analysis_df = pd.DataFrame({"Number of Unique Items" : [unique_items_count], "Average Price" : [avg_price], 
                                       "Number of Purchases" : [purchases_amt],"Total Revenue":[total_revenue]})
purchasing_analysis_df.style.format({'Average Price': '${:,.2f}','Total Revenue': '${:,.2f}'})


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[185]:


# Group purchase_data by Gender
gender = purchase_data.groupby('Gender')

# Count the total of screen names "SN" by gender
total_gender_count = gender.nunique()['SN']

# Total count by gender and divivde by total players 
percentage_of_players = total_gender_count / total_player_count * 100

# Create data frame with obtained values
demographics_df = pd.DataFrame({'Total Count': total_count_gender,'Percentage Of Players': percentage_of_players})

# Format the data frame with no index name in the corner
demographics_df.index.name = None

# Format the values sorted by total count in descending order, and two decimal places for the percentage
demographics_df.sort_values(['Total Count'], ascending = False).style.format({'Percentage Of Players':'{:.2f}%'})


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[186]:


purchase_count = gender['Purchase ID'].count()
avg_purchase_price = gender['Price'].mean()
avg_purchase_total = gender['Price'].sum()
avg_purchase_total_per_person = avg_purchase_total/total_gender_count
gender_demographics_df = pd.DataFrame({'Purchase Count': purchase_count, 
                                       'Average Purchase Price': avg_purchase_price, 
                                       'Average Purchase Total': avg_purchase_total,
                                    'Average Purchase Total Per Person': avg_purchase_total_per_person})
gender_demographics_df.sort_values(['Purchase Count'], ascending = False).style.format({"Average Purchase Total":"${:,.2f}",
                                                                                        "Average Purchase Price":"${:,.2f}",
                                                                                        "Average Purchase Total Per Person":"${:,.2f}"})


# Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[187]:


age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

purchase_data["Age Group"] = pd.cut(purchase_data["Age"],age_bins, labels=group_names)
purchase_data

age_grouped = purchase_data.groupby("Age Group")

total_count_age = age_grouped["SN"].nunique()

percentage_by_age = (total_count_age/total_player_count) * 100

age_demographics = pd.DataFrame({"Percentage of Players": percentage_by_age, "Total Count": total_count_age})

age_demographics.index.name = None

age_demographics.style.format({"Percentage of Players":"{:,.2f}"})


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[188]:


purchase_count_age = age_grouped["Purchase ID"].count()

avg_purchase_price_age = age_grouped["Price"].mean()
 
total_purchase_value = age_grouped["Price"].sum()

avg_purchase_per_person_age = total_purchase_value/total_count_age

age_demographics = pd.DataFrame({"Purchase Count": purchase_count_age,
                                 "Average Purchase Price": avg_purchase_price_age,
                                 "Total Purchase Value":total_purchase_value,
                                 "Average Purchase Total per Person": avg_purchase_per_person_age})

age_demographics.index.name = None

age_demographics.style.format({"Average Purchase Price":"${:,.2f}",
                               "Total Purchase Value":"${:,.2f}",
                               "Average Purchase Total per Person":"${:,.2f}"})


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[189]:


spender_info = purchase_data.groupby('SN')
spender_purchase_count = spender_info['Purchase ID'].count()
avg_spender_purchase_price = spender_info['Price'].mean()
total_purchase_value = spender_info['Price'].sum()

top_spenders_df = pd.DataFrame({'Purchase Count': spender_purchase_count, 'Average Purchase Price': avg_spender_purchase_price, 
                             'Total Purchase Value': total_purchase_value})
spenders_formatted = top_spenders_df.sort_values(['Total Purchase Value'], ascending = False).head()

spenders_formatted.style.format({'Average Purchase Price': '${:,.2f}', 'Total Purchase Value': '${:,.2f}'})


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, average item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[193]:


items = purchase_data[['Item ID', 'Item Name', 'Price']]
item_data = items.groupby(['Item ID', 'Item Name'])
purchase_count = item_data['Price'].count()
total_purchase_value = (item_data['Price'].sum())

avg_item_price = total_purchase_value/purchase_count

popular_items_df = pd.DataFrame({'Purchase Count': purchase_count, 'Item Price': avg_item_price, 'Total Purchase Value': total_purchase_value})

items_formatted = popular_items_df.sort_values(['Purchase Count'], ascending = False).head()

items_formatted.style.format({'Item Price': '${:,.2f}',
                              'Total Purchase Value': '${:,.2f}'})


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[195]:


items_formatted = popular_items_df.sort_values(['Total Purchase Value'], ascending = False).head()

items_formatted.style.format({'Item Price': '${:,.2f}',
                              'Total Purchase Value': '${:,.2f}'})


# In[ ]:




