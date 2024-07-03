# Analyze the distribution of product categories
product_distribution = data['Category'].value_counts()

# Plot product distribution
product_distribution.plot(kind='bar', figsize=(10,6))
plt.title('Product Category Distribution')
plt.xlabel('Category')
plt.ylabel('Frequency')
plt.show()

# Analyze the distribution of product sizes
size_distribution = data['Size'].value_counts()

# Plot size distribution
size_distribution.plot(kind='bar', figsize=(10,6))
plt.title('Product Size Distribution')
plt.xlabel('Size')
plt.ylabel('Frequency')
plt.show()
