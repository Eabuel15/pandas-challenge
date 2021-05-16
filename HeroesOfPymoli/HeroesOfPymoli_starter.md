### Note
* Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.


```python
# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase ID</th>
      <th>SN</th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Lisim78</td>
      <td>20</td>
      <td>Male</td>
      <td>108</td>
      <td>Extraction, Quickblade Of Trembling Hands</td>
      <td>3.53</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Lisovynya38</td>
      <td>40</td>
      <td>Male</td>
      <td>143</td>
      <td>Frenzied Scimitar</td>
      <td>1.56</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Ithergue48</td>
      <td>24</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>4.88</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Chamassasya86</td>
      <td>24</td>
      <td>Male</td>
      <td>100</td>
      <td>Blindscythe</td>
      <td>3.27</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Iskosia90</td>
      <td>23</td>
      <td>Male</td>
      <td>131</td>
      <td>Fury</td>
      <td>1.44</td>
    </tr>
  </tbody>
</table>
</div>



## Player Count

* Display the total number of players



```python
total_player_count = len(purchase_data["SN"].value_counts())
player_count_df = pd.DataFrame({"Total Players" : [total_player_count]})
player_count_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>576</td>
    </tr>
  </tbody>
</table>
</div>



## Purchasing Analysis (Total)

* Run basic calculations to obtain number of unique items, average price, etc.


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame



```python
unique_items_count = len(purchase_data["Item Name"].value_counts())
avg_price = purchase_data["Price"].mean()
purchases_amt = purchase_data["Purchase ID"].count()
total_revenue = sum(purchase_data["Price"])
purchasing_analysis_df = pd.DataFrame({"Number of Unique Items" : [unique_items_count], "Average Price" : [avg_price], 
                                       "Number of Purchases" : [purchases_amt],"Total Revenue":[total_revenue]})
purchasing_analysis_df.style.format({'Average Price': '${:,.2f}','Total Revenue': '${:,.2f}'})
```




<style  type="text/css" >
</style><table id="T_136da4d5_b5e8_11eb_a12e_d0577b86a497" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Number of Unique Items</th>        <th class="col_heading level0 col1" >Average Price</th>        <th class="col_heading level0 col2" >Number of Purchases</th>        <th class="col_heading level0 col3" >Total Revenue</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_136da4d5_b5e8_11eb_a12e_d0577b86a497level0_row0" class="row_heading level0 row0" >0</th>
                        <td id="T_136da4d5_b5e8_11eb_a12e_d0577b86a497row0_col0" class="data row0 col0" >179</td>
                        <td id="T_136da4d5_b5e8_11eb_a12e_d0577b86a497row0_col1" class="data row0 col1" >$3.05</td>
                        <td id="T_136da4d5_b5e8_11eb_a12e_d0577b86a497row0_col2" class="data row0 col2" >780</td>
                        <td id="T_136da4d5_b5e8_11eb_a12e_d0577b86a497row0_col3" class="data row0 col3" >$2,379.77</td>
            </tr>
    </tbody></table>



## Gender Demographics

* Percentage and Count of Male Players


* Percentage and Count of Female Players


* Percentage and Count of Other / Non-Disclosed





```python
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
```




<style  type="text/css" >
</style><table id="T_137b7e15_b5e8_11eb_bff0_d0577b86a497" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Total Count</th>        <th class="col_heading level0 col1" >Percentage Of Players</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_137b7e15_b5e8_11eb_bff0_d0577b86a497level0_row0" class="row_heading level0 row0" >Male</th>
                        <td id="T_137b7e15_b5e8_11eb_bff0_d0577b86a497row0_col0" class="data row0 col0" >484</td>
                        <td id="T_137b7e15_b5e8_11eb_bff0_d0577b86a497row0_col1" class="data row0 col1" >84.03%</td>
            </tr>
            <tr>
                        <th id="T_137b7e15_b5e8_11eb_bff0_d0577b86a497level0_row1" class="row_heading level0 row1" >Female</th>
                        <td id="T_137b7e15_b5e8_11eb_bff0_d0577b86a497row1_col0" class="data row1 col0" >81</td>
                        <td id="T_137b7e15_b5e8_11eb_bff0_d0577b86a497row1_col1" class="data row1 col1" >14.06%</td>
            </tr>
            <tr>
                        <th id="T_137b7e15_b5e8_11eb_bff0_d0577b86a497level0_row2" class="row_heading level0 row2" >Other / Non-Disclosed</th>
                        <td id="T_137b7e15_b5e8_11eb_bff0_d0577b86a497row2_col0" class="data row2 col0" >11</td>
                        <td id="T_137b7e15_b5e8_11eb_bff0_d0577b86a497row2_col1" class="data row2 col1" >1.91%</td>
            </tr>
    </tbody></table>




## Purchasing Analysis (Gender)

* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender




* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame


```python
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
```




<style  type="text/css" >
</style><table id="T_13869a13_b5e8_11eb_8445_d0577b86a497" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Purchase Count</th>        <th class="col_heading level0 col1" >Average Purchase Price</th>        <th class="col_heading level0 col2" >Average Purchase Total</th>        <th class="col_heading level0 col3" >Average Purchase Total Per Person</th>    </tr>    <tr>        <th class="index_name level0" >Gender</th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_13869a13_b5e8_11eb_8445_d0577b86a497level0_row0" class="row_heading level0 row0" >Male</th>
                        <td id="T_13869a13_b5e8_11eb_8445_d0577b86a497row0_col0" class="data row0 col0" >652</td>
                        <td id="T_13869a13_b5e8_11eb_8445_d0577b86a497row0_col1" class="data row0 col1" >$3.02</td>
                        <td id="T_13869a13_b5e8_11eb_8445_d0577b86a497row0_col2" class="data row0 col2" >$1,967.64</td>
                        <td id="T_13869a13_b5e8_11eb_8445_d0577b86a497row0_col3" class="data row0 col3" >$4.07</td>
            </tr>
            <tr>
                        <th id="T_13869a13_b5e8_11eb_8445_d0577b86a497level0_row1" class="row_heading level0 row1" >Female</th>
                        <td id="T_13869a13_b5e8_11eb_8445_d0577b86a497row1_col0" class="data row1 col0" >113</td>
                        <td id="T_13869a13_b5e8_11eb_8445_d0577b86a497row1_col1" class="data row1 col1" >$3.20</td>
                        <td id="T_13869a13_b5e8_11eb_8445_d0577b86a497row1_col2" class="data row1 col2" >$361.94</td>
                        <td id="T_13869a13_b5e8_11eb_8445_d0577b86a497row1_col3" class="data row1 col3" >$4.47</td>
            </tr>
            <tr>
                        <th id="T_13869a13_b5e8_11eb_8445_d0577b86a497level0_row2" class="row_heading level0 row2" >Other / Non-Disclosed</th>
                        <td id="T_13869a13_b5e8_11eb_8445_d0577b86a497row2_col0" class="data row2 col0" >15</td>
                        <td id="T_13869a13_b5e8_11eb_8445_d0577b86a497row2_col1" class="data row2 col1" >$3.35</td>
                        <td id="T_13869a13_b5e8_11eb_8445_d0577b86a497row2_col2" class="data row2 col2" >$50.19</td>
                        <td id="T_13869a13_b5e8_11eb_8445_d0577b86a497row2_col3" class="data row2 col3" >$4.56</td>
            </tr>
    </tbody></table>



Age Demographics

* Establish bins for ages


* Categorize the existing players using the age bins. Hint: use pd.cut()


* Calculate the numbers and percentages by age group


* Create a summary data frame to hold the results


* Optional: round the percentage column to two decimal points


* Display Age Demographics Table



```python
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
```




<style  type="text/css" >
</style><table id="T_13936283_b5e8_11eb_9615_d0577b86a497" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Percentage of Players</th>        <th class="col_heading level0 col1" >Total Count</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_13936283_b5e8_11eb_9615_d0577b86a497level0_row0" class="row_heading level0 row0" ><10</th>
                        <td id="T_13936283_b5e8_11eb_9615_d0577b86a497row0_col0" class="data row0 col0" >2.95</td>
                        <td id="T_13936283_b5e8_11eb_9615_d0577b86a497row0_col1" class="data row0 col1" >17</td>
            </tr>
            <tr>
                        <th id="T_13936283_b5e8_11eb_9615_d0577b86a497level0_row1" class="row_heading level0 row1" >10-14</th>
                        <td id="T_13936283_b5e8_11eb_9615_d0577b86a497row1_col0" class="data row1 col0" >3.82</td>
                        <td id="T_13936283_b5e8_11eb_9615_d0577b86a497row1_col1" class="data row1 col1" >22</td>
            </tr>
            <tr>
                        <th id="T_13936283_b5e8_11eb_9615_d0577b86a497level0_row2" class="row_heading level0 row2" >15-19</th>
                        <td id="T_13936283_b5e8_11eb_9615_d0577b86a497row2_col0" class="data row2 col0" >18.58</td>
                        <td id="T_13936283_b5e8_11eb_9615_d0577b86a497row2_col1" class="data row2 col1" >107</td>
            </tr>
            <tr>
                        <th id="T_13936283_b5e8_11eb_9615_d0577b86a497level0_row3" class="row_heading level0 row3" >20-24</th>
                        <td id="T_13936283_b5e8_11eb_9615_d0577b86a497row3_col0" class="data row3 col0" >44.79</td>
                        <td id="T_13936283_b5e8_11eb_9615_d0577b86a497row3_col1" class="data row3 col1" >258</td>
            </tr>
            <tr>
                        <th id="T_13936283_b5e8_11eb_9615_d0577b86a497level0_row4" class="row_heading level0 row4" >25-29</th>
                        <td id="T_13936283_b5e8_11eb_9615_d0577b86a497row4_col0" class="data row4 col0" >13.37</td>
                        <td id="T_13936283_b5e8_11eb_9615_d0577b86a497row4_col1" class="data row4 col1" >77</td>
            </tr>
            <tr>
                        <th id="T_13936283_b5e8_11eb_9615_d0577b86a497level0_row5" class="row_heading level0 row5" >30-34</th>
                        <td id="T_13936283_b5e8_11eb_9615_d0577b86a497row5_col0" class="data row5 col0" >9.03</td>
                        <td id="T_13936283_b5e8_11eb_9615_d0577b86a497row5_col1" class="data row5 col1" >52</td>
            </tr>
            <tr>
                        <th id="T_13936283_b5e8_11eb_9615_d0577b86a497level0_row6" class="row_heading level0 row6" >35-39</th>
                        <td id="T_13936283_b5e8_11eb_9615_d0577b86a497row6_col0" class="data row6 col0" >5.38</td>
                        <td id="T_13936283_b5e8_11eb_9615_d0577b86a497row6_col1" class="data row6 col1" >31</td>
            </tr>
            <tr>
                        <th id="T_13936283_b5e8_11eb_9615_d0577b86a497level0_row7" class="row_heading level0 row7" >40+</th>
                        <td id="T_13936283_b5e8_11eb_9615_d0577b86a497row7_col0" class="data row7 col0" >2.08</td>
                        <td id="T_13936283_b5e8_11eb_9615_d0577b86a497row7_col1" class="data row7 col1" >12</td>
            </tr>
    </tbody></table>



## Purchasing Analysis (Age)

* Bin the purchase_data data frame by age


* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame


```python
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
```




<style  type="text/css" >
</style><table id="T_139e0996_b5e8_11eb_899d_d0577b86a497" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Purchase Count</th>        <th class="col_heading level0 col1" >Average Purchase Price</th>        <th class="col_heading level0 col2" >Total Purchase Value</th>        <th class="col_heading level0 col3" >Average Purchase Total per Person</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_139e0996_b5e8_11eb_899d_d0577b86a497level0_row0" class="row_heading level0 row0" ><10</th>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row0_col0" class="data row0 col0" >23</td>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row0_col1" class="data row0 col1" >$3.35</td>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row0_col2" class="data row0 col2" >$77.13</td>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row0_col3" class="data row0 col3" >$4.54</td>
            </tr>
            <tr>
                        <th id="T_139e0996_b5e8_11eb_899d_d0577b86a497level0_row1" class="row_heading level0 row1" >10-14</th>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row1_col0" class="data row1 col0" >28</td>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row1_col1" class="data row1 col1" >$2.96</td>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row1_col2" class="data row1 col2" >$82.78</td>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row1_col3" class="data row1 col3" >$3.76</td>
            </tr>
            <tr>
                        <th id="T_139e0996_b5e8_11eb_899d_d0577b86a497level0_row2" class="row_heading level0 row2" >15-19</th>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row2_col0" class="data row2 col0" >136</td>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row2_col1" class="data row2 col1" >$3.04</td>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row2_col2" class="data row2 col2" >$412.89</td>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row2_col3" class="data row2 col3" >$3.86</td>
            </tr>
            <tr>
                        <th id="T_139e0996_b5e8_11eb_899d_d0577b86a497level0_row3" class="row_heading level0 row3" >20-24</th>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row3_col0" class="data row3 col0" >365</td>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row3_col1" class="data row3 col1" >$3.05</td>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row3_col2" class="data row3 col2" >$1,114.06</td>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row3_col3" class="data row3 col3" >$4.32</td>
            </tr>
            <tr>
                        <th id="T_139e0996_b5e8_11eb_899d_d0577b86a497level0_row4" class="row_heading level0 row4" >25-29</th>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row4_col0" class="data row4 col0" >101</td>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row4_col1" class="data row4 col1" >$2.90</td>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row4_col2" class="data row4 col2" >$293.00</td>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row4_col3" class="data row4 col3" >$3.81</td>
            </tr>
            <tr>
                        <th id="T_139e0996_b5e8_11eb_899d_d0577b86a497level0_row5" class="row_heading level0 row5" >30-34</th>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row5_col0" class="data row5 col0" >73</td>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row5_col1" class="data row5 col1" >$2.93</td>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row5_col2" class="data row5 col2" >$214.00</td>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row5_col3" class="data row5 col3" >$4.12</td>
            </tr>
            <tr>
                        <th id="T_139e0996_b5e8_11eb_899d_d0577b86a497level0_row6" class="row_heading level0 row6" >35-39</th>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row6_col0" class="data row6 col0" >41</td>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row6_col1" class="data row6 col1" >$3.60</td>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row6_col2" class="data row6 col2" >$147.67</td>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row6_col3" class="data row6 col3" >$4.76</td>
            </tr>
            <tr>
                        <th id="T_139e0996_b5e8_11eb_899d_d0577b86a497level0_row7" class="row_heading level0 row7" >40+</th>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row7_col0" class="data row7 col0" >13</td>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row7_col1" class="data row7 col1" >$2.94</td>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row7_col2" class="data row7 col2" >$38.24</td>
                        <td id="T_139e0996_b5e8_11eb_899d_d0577b86a497row7_col3" class="data row7 col3" >$3.19</td>
            </tr>
    </tbody></table>



## Top Spenders

* Run basic calculations to obtain the results in the table below


* Create a summary data frame to hold the results


* Sort the total purchase value column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame




```python
spender_info = purchase_data.groupby('SN')
spender_purchase_count = spender_info['Purchase ID'].count()
avg_spender_purchase_price = spender_info['Price'].mean()
total_purchase_value = spender_info['Price'].sum()

top_spenders_df = pd.DataFrame({'Purchase Count': spender_purchase_count, 'Average Purchase Price': avg_spender_purchase_price, 
                             'Total Purchase Value': total_purchase_value})
spenders_formatted = top_spenders_df.sort_values(['Total Purchase Value'], ascending = False).head()

spenders_formatted.style.format({'Average Purchase Price': '${:,.2f}', 'Total Purchase Value': '${:,.2f}'})
```




<style  type="text/css" >
</style><table id="T_13aa8438_b5e8_11eb_8b1d_d0577b86a497" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Purchase Count</th>        <th class="col_heading level0 col1" >Average Purchase Price</th>        <th class="col_heading level0 col2" >Total Purchase Value</th>    </tr>    <tr>        <th class="index_name level0" >SN</th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_13aa8438_b5e8_11eb_8b1d_d0577b86a497level0_row0" class="row_heading level0 row0" >Lisosia93</th>
                        <td id="T_13aa8438_b5e8_11eb_8b1d_d0577b86a497row0_col0" class="data row0 col0" >5</td>
                        <td id="T_13aa8438_b5e8_11eb_8b1d_d0577b86a497row0_col1" class="data row0 col1" >$3.79</td>
                        <td id="T_13aa8438_b5e8_11eb_8b1d_d0577b86a497row0_col2" class="data row0 col2" >$18.96</td>
            </tr>
            <tr>
                        <th id="T_13aa8438_b5e8_11eb_8b1d_d0577b86a497level0_row1" class="row_heading level0 row1" >Idastidru52</th>
                        <td id="T_13aa8438_b5e8_11eb_8b1d_d0577b86a497row1_col0" class="data row1 col0" >4</td>
                        <td id="T_13aa8438_b5e8_11eb_8b1d_d0577b86a497row1_col1" class="data row1 col1" >$3.86</td>
                        <td id="T_13aa8438_b5e8_11eb_8b1d_d0577b86a497row1_col2" class="data row1 col2" >$15.45</td>
            </tr>
            <tr>
                        <th id="T_13aa8438_b5e8_11eb_8b1d_d0577b86a497level0_row2" class="row_heading level0 row2" >Chamjask73</th>
                        <td id="T_13aa8438_b5e8_11eb_8b1d_d0577b86a497row2_col0" class="data row2 col0" >3</td>
                        <td id="T_13aa8438_b5e8_11eb_8b1d_d0577b86a497row2_col1" class="data row2 col1" >$4.61</td>
                        <td id="T_13aa8438_b5e8_11eb_8b1d_d0577b86a497row2_col2" class="data row2 col2" >$13.83</td>
            </tr>
            <tr>
                        <th id="T_13aa8438_b5e8_11eb_8b1d_d0577b86a497level0_row3" class="row_heading level0 row3" >Iral74</th>
                        <td id="T_13aa8438_b5e8_11eb_8b1d_d0577b86a497row3_col0" class="data row3 col0" >4</td>
                        <td id="T_13aa8438_b5e8_11eb_8b1d_d0577b86a497row3_col1" class="data row3 col1" >$3.40</td>
                        <td id="T_13aa8438_b5e8_11eb_8b1d_d0577b86a497row3_col2" class="data row3 col2" >$13.62</td>
            </tr>
            <tr>
                        <th id="T_13aa8438_b5e8_11eb_8b1d_d0577b86a497level0_row4" class="row_heading level0 row4" >Iskadarya95</th>
                        <td id="T_13aa8438_b5e8_11eb_8b1d_d0577b86a497row4_col0" class="data row4 col0" >3</td>
                        <td id="T_13aa8438_b5e8_11eb_8b1d_d0577b86a497row4_col1" class="data row4 col1" >$4.37</td>
                        <td id="T_13aa8438_b5e8_11eb_8b1d_d0577b86a497row4_col2" class="data row4 col2" >$13.10</td>
            </tr>
    </tbody></table>



## Most Popular Items

* Retrieve the Item ID, Item Name, and Item Price columns


* Group by Item ID and Item Name. Perform calculations to obtain purchase count, average item price, and total purchase value


* Create a summary data frame to hold the results


* Sort the purchase count column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame




```python
items = purchase_data[['Item ID', 'Item Name', 'Price']]
item_data = items.groupby(['Item ID', 'Item Name'])
purchase_count = item_data['Price'].count()
total_purchase_value = (item_data['Price'].sum())

avg_item_price = total_purchase_value/purchase_count

popular_items_df = pd.DataFrame({'Purchase Count': purchase_count, 'Item Price': avg_item_price, 'Total Purchase Value': total_purchase_value})

items_formatted = popular_items_df.sort_values(['Purchase Count'], ascending = False).head()

items_formatted.style.format({'Item Price': '${:,.2f}',
                              'Total Purchase Value': '${:,.2f}'})

```




<style  type="text/css" >
</style><table id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497" ><thead>    <tr>        <th class="blank" ></th>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Purchase Count</th>        <th class="col_heading level0 col1" >Item Price</th>        <th class="col_heading level0 col2" >Total Purchase Value</th>    </tr>    <tr>        <th class="index_name level0" >Item ID</th>        <th class="index_name level1" >Item Name</th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497level0_row0" class="row_heading level0 row0" >92</th>
                        <th id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497level1_row0" class="row_heading level1 row0" >Final Critic</th>
                        <td id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497row0_col0" class="data row0 col0" >13</td>
                        <td id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497row0_col1" class="data row0 col1" >$4.61</td>
                        <td id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497row0_col2" class="data row0 col2" >$59.99</td>
            </tr>
            <tr>
                        <th id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497level0_row1" class="row_heading level0 row1" >178</th>
                        <th id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497level1_row1" class="row_heading level1 row1" >Oathbreaker, Last Hope of the Breaking Storm</th>
                        <td id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497row1_col0" class="data row1 col0" >12</td>
                        <td id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497row1_col1" class="data row1 col1" >$4.23</td>
                        <td id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497row1_col2" class="data row1 col2" >$50.76</td>
            </tr>
            <tr>
                        <th id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497level0_row2" class="row_heading level0 row2" >145</th>
                        <th id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497level1_row2" class="row_heading level1 row2" >Fiery Glass Crusader</th>
                        <td id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497row2_col0" class="data row2 col0" >9</td>
                        <td id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497row2_col1" class="data row2 col1" >$4.58</td>
                        <td id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497row2_col2" class="data row2 col2" >$41.22</td>
            </tr>
            <tr>
                        <th id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497level0_row3" class="row_heading level0 row3" >132</th>
                        <th id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497level1_row3" class="row_heading level1 row3" >Persuasion</th>
                        <td id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497row3_col0" class="data row3 col0" >9</td>
                        <td id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497row3_col1" class="data row3 col1" >$3.22</td>
                        <td id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497row3_col2" class="data row3 col2" >$28.99</td>
            </tr>
            <tr>
                        <th id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497level0_row4" class="row_heading level0 row4" >108</th>
                        <th id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497level1_row4" class="row_heading level1 row4" >Extraction, Quickblade Of Trembling Hands</th>
                        <td id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497row4_col0" class="data row4 col0" >9</td>
                        <td id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497row4_col1" class="data row4 col1" >$3.53</td>
                        <td id="T_47a45503_b5e8_11eb_9ecb_d0577b86a497row4_col2" class="data row4 col2" >$31.77</td>
            </tr>
    </tbody></table>



## Most Profitable Items

* Sort the above table by total purchase value in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the data frame




```python
items_formatted = popular_items_df.sort_values(['Total Purchase Value'], ascending = False).head()

items_formatted.style.format({'Item Price': '${:,.2f}',
                              'Total Purchase Value': '${:,.2f}'})
```




<style  type="text/css" >
</style><table id="T_87942c39_b5e8_11eb_8039_d0577b86a497" ><thead>    <tr>        <th class="blank" ></th>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Purchase Count</th>        <th class="col_heading level0 col1" >Item Price</th>        <th class="col_heading level0 col2" >Total Purchase Value</th>    </tr>    <tr>        <th class="index_name level0" >Item ID</th>        <th class="index_name level1" >Item Name</th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_87942c39_b5e8_11eb_8039_d0577b86a497level0_row0" class="row_heading level0 row0" >92</th>
                        <th id="T_87942c39_b5e8_11eb_8039_d0577b86a497level1_row0" class="row_heading level1 row0" >Final Critic</th>
                        <td id="T_87942c39_b5e8_11eb_8039_d0577b86a497row0_col0" class="data row0 col0" >13</td>
                        <td id="T_87942c39_b5e8_11eb_8039_d0577b86a497row0_col1" class="data row0 col1" >$4.61</td>
                        <td id="T_87942c39_b5e8_11eb_8039_d0577b86a497row0_col2" class="data row0 col2" >$59.99</td>
            </tr>
            <tr>
                        <th id="T_87942c39_b5e8_11eb_8039_d0577b86a497level0_row1" class="row_heading level0 row1" >178</th>
                        <th id="T_87942c39_b5e8_11eb_8039_d0577b86a497level1_row1" class="row_heading level1 row1" >Oathbreaker, Last Hope of the Breaking Storm</th>
                        <td id="T_87942c39_b5e8_11eb_8039_d0577b86a497row1_col0" class="data row1 col0" >12</td>
                        <td id="T_87942c39_b5e8_11eb_8039_d0577b86a497row1_col1" class="data row1 col1" >$4.23</td>
                        <td id="T_87942c39_b5e8_11eb_8039_d0577b86a497row1_col2" class="data row1 col2" >$50.76</td>
            </tr>
            <tr>
                        <th id="T_87942c39_b5e8_11eb_8039_d0577b86a497level0_row2" class="row_heading level0 row2" >82</th>
                        <th id="T_87942c39_b5e8_11eb_8039_d0577b86a497level1_row2" class="row_heading level1 row2" >Nirvana</th>
                        <td id="T_87942c39_b5e8_11eb_8039_d0577b86a497row2_col0" class="data row2 col0" >9</td>
                        <td id="T_87942c39_b5e8_11eb_8039_d0577b86a497row2_col1" class="data row2 col1" >$4.90</td>
                        <td id="T_87942c39_b5e8_11eb_8039_d0577b86a497row2_col2" class="data row2 col2" >$44.10</td>
            </tr>
            <tr>
                        <th id="T_87942c39_b5e8_11eb_8039_d0577b86a497level0_row3" class="row_heading level0 row3" >145</th>
                        <th id="T_87942c39_b5e8_11eb_8039_d0577b86a497level1_row3" class="row_heading level1 row3" >Fiery Glass Crusader</th>
                        <td id="T_87942c39_b5e8_11eb_8039_d0577b86a497row3_col0" class="data row3 col0" >9</td>
                        <td id="T_87942c39_b5e8_11eb_8039_d0577b86a497row3_col1" class="data row3 col1" >$4.58</td>
                        <td id="T_87942c39_b5e8_11eb_8039_d0577b86a497row3_col2" class="data row3 col2" >$41.22</td>
            </tr>
            <tr>
                        <th id="T_87942c39_b5e8_11eb_8039_d0577b86a497level0_row4" class="row_heading level0 row4" >103</th>
                        <th id="T_87942c39_b5e8_11eb_8039_d0577b86a497level1_row4" class="row_heading level1 row4" >Singed Scalpel</th>
                        <td id="T_87942c39_b5e8_11eb_8039_d0577b86a497row4_col0" class="data row4 col0" >8</td>
                        <td id="T_87942c39_b5e8_11eb_8039_d0577b86a497row4_col1" class="data row4 col1" >$4.35</td>
                        <td id="T_87942c39_b5e8_11eb_8039_d0577b86a497row4_col2" class="data row4 col2" >$34.80</td>
            </tr>
    </tbody></table>




```python

```
