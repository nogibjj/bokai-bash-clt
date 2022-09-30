#  Bash Command-Line Tool

__Author: Bokai Zhou__

This is the second individual project of building a Bash command-line tool to perform useful data preparation tasks. 

### Dataset: [Walmart Sales Dataset of 45stores](https://www.kaggle.com/datasets/varsharam/walmart-sales-dataset-of-45stores?resource=download)
- __Store__: Store Numbers ranging from 1 to 45
- __Date__: The Week of Sales. It is in the format of dd-mm-yyyy. The date starts from 05-02-2010
- __Weekly_Sales__: The sales of the given store in the given week
- __Holiday_Flag__: If the week has a special Holiday or not. 1-The week has a Holiday 0-Fully working week Holiday events is given in
- __Temperature__: Average Temperature of the week of sales
- __Fuel_Price__: Price of the Fuel in the region of the given store
- __CPI__: Customer Price Index
- __Unemployment__: Unemployment of the given store region

### Command lines:
- describe: Load the data and print the description in the terminal

- find-store: Find all data of a specific store

  Argument: --store, default="1", the store number ranging from 1 to 45
  
- find-date: Find all data before or after a specific date

  Arguments: 
  1. --y, default="2010", Year of the date, default 2010
  2. --m, default="01", Month of the date, default 01
  3. --d, default="01", Day of the date, default 01
  4. --b, default="1", Whether before the date or not, if 1 then before, otherwise after
             
- holiday: Find the data within/without the special holiday week.

  Arguments: --h, default="1", Whether a holiday. If 1 then holiday, if 0 not.
  
- sort: Sort the data ascending/desceding by a chosen column.

  Arguments: 
  1. --r, default="1", Index of row sorted by. If 1 then sort by the first row.
  2. --asc, default="1", If 1 then ascending, if 0 descending.
