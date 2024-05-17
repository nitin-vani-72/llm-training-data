import pandas as pd

# Step 1: Reading CSV file
data = pd.read_csv('Sales_Data.csv')

# Step 2: Handling missing/currupt data and converting date to datetime format
missing_values = data.isnull().sum()
data.dropna(inplace=True)
data['Date'] = pd.to_datetime(data['Date'])

# Step 3: Calculating total sales and adding a new column for Year
data['Total_Sales'] = data['Quantity'] * data['Price']
data['Year'] = data['Date'].dt.year

# Step 4: Calculating total sales per store, monthy sales trends and top 3 best-selling products
total_sales_per_store = data.groupby('Store_ID')['Total_Sales'].sum()
year_with_highest_sales = data.groupby('Year')['Total_Sales'].sum().idxmax()
monthly_sales_trends = data[data['Year'] == year_with_highest_sales].groupby(data['Date'].dt.month)['Total_Sales'].sum()
top_3_products = data.groupby('Product_ID')['Total_Sales'].sum().nlargest(3)

# Printing the results
print("Sales Data:\n", data)
print("\nMissing Values:\n", missing_values)
print("\nTotal Sales per Store:\n", total_sales_per_store)
print("\nMonthly Sales Trends for the Year with Highest Sales ({}):\n".format(year_with_highest_sales), monthly_sales_trends)
print("\nTop 3 Best-selling Products Overall:\n", top_3_products)