import pandas as pd
import matplotlib.pyplot as plt

# 1. Load our clean data
df = pd.read_csv("clean_data.csv")

# 2. Create a Bar Chart: Item Name vs. Inventory
plt.figure(figsize=(10, 6)) # Set the size of the "Canvas"
plt.bar(df['Item_Name'], df['Inventory'], color='skyblue')

# 3. Add Labels (Like Webflow CMS field labels)
plt.title('Inventory Levels by Product', fontsize=14)
plt.xlabel('Product Name')
plt.ylabel('Quantity in Stock')

# 4. Save the chart as an image
plt.savefig('inventory_chart.png')
print("✅ Success: Chart saved as inventory_chart.png")

# 5. Show the chart (This will pop up a window on your computer!)
plt.show()