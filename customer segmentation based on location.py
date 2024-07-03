# Group by state and calculate total sales
state_sales = data.groupby('ship-state')['Amount'].sum().reset_index()

# Plot state sales distribution
state_sales.plot(kind='bar', x='ship-state', y='Amount', figsize=(12,8))
plt.title('State-wise Sales Distribution')
plt.xlabel('State')
plt.ylabel('Total Sales')
plt.show()
