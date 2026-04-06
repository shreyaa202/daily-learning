import pandas as pd

# 1. Load the CSV file (Think of this as "Importing" into a CMS)
df = pd.read_csv("webflow_export.csv")

print("--- 📦 Raw Webflow Export ---")
print(df.head()) # .head() shows the first 5 rows

# 2. The AI Engineer's Task: Find Out-of-Stock Items
# In Webflow, you'd hide these. In Python, we filter them.
out_of_stock = df[df["Inventory"] == 0]

print("\n--- ⚠️ Alert: Out of Stock Items ---")
if not out_of_stock.empty:
    print(out_of_stock[["Item_Name", "Category"]])
else:
    print("All items are in stock!")

# 3. Simple Calculation: What is the total value of our Apparel?
apparel_only = df[df["Category"] == "Apparel"]
total_value = (apparel_only["Price"] * apparel_only["Inventory"]).sum()

print(f"\nTotal Inventory Value (Apparel): ${total_value}")