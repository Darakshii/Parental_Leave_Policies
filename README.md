# Parental_Leave_Policies

**"Parental Leave Policies: A New Frontier in Employee Benefits"**
![plp](https://github.com/Darakshii/Parental_Leave_Policies/assets/130299461/4ad73a23-fe1f-4210-a564-03235b0cd1e1)

## Overview of the Data.
Crowdsourced parental leave data from 1,601 companies across different industries, including paid/unpaid maternity and paternity leave weeks.

* Company - Company name
* Industry - Company Industry & sub-industry (Industry: Sub-industry)
* Paid Maternity Leave-  Paid weeks off from work for mothers after the birth of their child
* Unpaid Maternity Leave-  Unpaid weeks off from work for mothers after the birth of their child
* Paid Paternity Leave-  Paid weeks off from work for fathers after the birth of their child
* Unpaid Paternity Leave-  Unpaid weeks off from work for fathers after the birth of their child

NOTE: This is user-reported data. Where users report conflicting information, consensus numbers (if any) or the median are shown. "N/A" means no information has been reported.

## Task
1. Which companies offer the most paid parental leave weeks?
2. Is maternity leave typically longer than paternity leave?
3. What is the distribution of parental leave weeks offered?
4. Are there noticeable differences between industries?


## Data Understanding
A dataset of 1600 records with 6 fields is a valuable resource for analysis. However, before any analysis can be performed, the data must be cleaned and preprocessed to ensure that it is accurate and consistent.

The data cleaning process involves identifying and correcting errors in the data, such as duplicate records, missing values, and incorrect data types.

## Data Preprocesssing
Replacing null values with 0 as we do not have data about the companies and filling null values with mean/median/mode will lead us to some wrong interpretation of data and results.
Also, doing some aggregate between the columns like sum and average to get the desired data.

## Data Visualization
Data Visualization is created by using matplot and seaborn liebrary. Some distributions are also visualized to get important insights of the data by using some statistical concepts.

## Conclusion
1. companies offer the most paid parental leave weeks are as follows - 
* Grant Thornton 
* LAC-Group
* Flatiron Health
* Cloudworkers
* LeverX
* Rangle.io
* Washburn Center For Children
* Salesforce
* JHC Systems
* Dynatrace

2. As we can see in the above scatter plot, most of the company is providing Maternity Leave and does not offers Paternity leave or while some of the companies provide less paternity leave than maternity leave.So, We can say Maternity Leave is longer than Paternity Leave.
3.  Distribution of both Maternity and Paternity Leave is almost seems like normal distribution with very less skewed to the right.std for maternity leave is greater than paternity leave. and spread of the data in maternity leave is more and wide than that of paternity leave as more than 50% data in paternity leave is very close to mean. And in maternity data the data is spreaded over some std value.
4.  In every Industry Paid Maternity leave is longer than Paid Paternity leave.
5. Also Unpaid Maternity Leave is longer than Unpaid Paternity Leave.
6. Only Pharmacies and Drug Stores offers equal Unpaid Maternity as well as Paternity Leave.
7. Printing Industry offers same weeks of Paid Maternity and Paternity Leave. Also it offers highest no. of unpaid week leave
