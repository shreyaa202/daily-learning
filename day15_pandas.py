import pandas as pd

# 1. Creating a dataset (Imagine this is a Webflow CMS Export)
data = {
    "Page_Title": ["Home", "About", "Services", "Contact", "Blog"],
    "Views": [1200, 450, 800, 300, 2500],
    "Status": ["Published", "Published", "Draft", "Published", "Published"]
}

# 2. Turn it into a DataFrame (A powerful Python Table)
df = pd.DataFrame(data)

print("--- 📊 Webflow Site Analytics ---")
print(df)

# 3. Simple Analysis
print("\n--- Quick Stats ---")
print(f"Total Views: {df['Views'].sum()}")
print(f"Most Viewed Page: {df.iloc[df['Views'].idxmax()]['Page_Title']}")

# 4. Filtering (Show only Published pages)
published_pages = df[df["Status"] == "Published"]
print("\n--- Published Pages Only ---")
print(published_pages)