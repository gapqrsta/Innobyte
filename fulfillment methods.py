# Analyze fulfillment methods
fulfillment_analysis = data['Fulfilment'].value_counts()

# Plot fulfillment methods
fulfillment_analysis.plot(kind='bar', figsize=(10,6))
plt.title('Fulfillment Method Distribution')
plt.xlabel('Fulfillment Method')
plt.ylabel('Frequency')
plt.show()
