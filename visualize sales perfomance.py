import matplotlib.pyplot as plt

# Extract year and month from Date
data['YearMonth'] = data['Date'].dt.to_period('M')

# Group by YearMonth and calculate total sales
monthly_sales = data.groupby('YearMonth')['Amount'].sum().reset_index()

# Plot monthly sales
plt.figure(figsize=(10,6))
plt.plot(monthly_sales['YearMonth'].astype(str), monthly_sales['Amount'])
plt.title('Monthly Sales Performance')
plt.xlabel('Month')
plt.ylabel('Sales Amount')
plt.xticks(rotation=45)
plt.show()
