# --- DAY 9: LIST COMPREHENSIONS ---

# 1. The "Messy" Data (Common in web scraping)
raw_keywords = ["  python ", "ai engineer", "   MACHINE learning", " LLM ", "prompt "]

# 2. The "Old Way" (Using a standard loop)
cleaned_loop = []
for k in raw_keywords:
    cleaned_loop.append(k.strip().lower())

# 3. The "Pythonic Way" (List Comprehension)
# Format: [action FOR item IN list]
cleaned_fast = [k.strip().lower() for k in raw_keywords]

print("--- Data Cleaning Result ---")
print(f"Original: {raw_keywords}")
print(f"Cleaned:  {cleaned_fast}")

# 4. Adding a Filter (Only keep words longer than 3 characters)
filtered_keywords = [k for k in cleaned_fast if len(k) > 3]
print(f"Filtered: {filtered_keywords}")