# --- DAY 8: FILE I/O (INPUT/OUTPUT) ---

# 1. Reading the entire file
print("--- Reading Full File ---")
with open("knowledge_base.txt", "r") as file:
    content = file.read()
    print(content)

# 2. Reading line by line (Great for large datasets)
print("\n--- Reading Line by Line ---")
with open("knowledge_base.txt", "r") as file:
    for line in file:
        # .strip() removes the extra newline at the end of each line
        print(f"Processing: {line.strip()}")

# 3. Writing to a new file
print("\n--- Writing a Status Report ---")
with open("report.txt", "w") as report:
    report.write("Day 8 Task: Completed\n")
    report.write("Status: I can now read and write files!")

print("Report saved to report.txt")