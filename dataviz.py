import matplotlib.pyplot as plt

# Example visualization: Units sold over time by category
plt.figure(figsize=(10, 6))
for category in df['Category'].unique():
    subset = df[df['Category'] == category]
    plt.plot(subset['Date'], subset['Units_Sold'], label=category)

plt.xlabel('Date')
plt.ylabel('Units Sold')
plt.title('Units Sold Over Time by Category')
plt.legend()
plt.grid(True)
plt.show()