# --- DAY 5: DICTIONARIES (CMS ITEMS) ---

# 1. Creating a Dictionary
# It uses curly braces { } and 'Key': 'Value' pairs
project = {
    "client_name": "Sindur Beauty Parlor",
    "pages": 5,
    "has_cms": True,
    "status": "In Progress"
}

# 2. Accessing data (using the Key)
print(f"Working on project for: {project['client_name']}")

# 3. Updating a value
project["status"] = "Completed"
print(f"Project Status updated to: {project['status']}")

# 4. Adding a new key (like adding a field in Webflow CMS)
project["technology"] = "React & AI"

# 5. Looping through a dictionary
print("\n--- Project Details ---")
for key, value in project.items():
    print(f"{key.capitalize()}: {value}")