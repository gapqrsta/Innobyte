# Analyze the distribution of product categories
product_distribution = data['Category'].value_counts()

# Plot product distribution
product_distribution.plot(kind='bar', figsize=(10,6))
plt.title('Product Category Distribution')
plt.xlabel('Category')
plt.ylabel('Frequency')
plt.show()
