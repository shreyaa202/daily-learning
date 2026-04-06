import pandas as pd

# 1. Load the messy data
df = pd.read_csv("messy_data.csv")

print("--- 🗑️ Before Cleaning ---")
print(df)

# 2. Fix Extra Spaces (Trimming)
# Just like in Webflow, spaces can break search!
df['Item_Name'] = df['Item_Name'].str.strip()

# 3. Handle Missing Values
# Fill missing Price with 0 and replace "None" strings
df['Price'] = pd.to_numeric(df['Price'], errors='coerce').fillna(0)
df['Inventory'] = pd.to_numeric(df['Inventory'], errors='coerce').fillna(0)

print("\n--- ✨ After Cleaning ---")
print(df)

# 4. Save the Clean Version
df.to_csv("clean_data.csv", index=False)
print("\n✅ Success: Clean data saved to clean_data.csv")