# --- DAY 3: LISTS & LOOPS ---

# 1. Creating a List (Like a CMS Collection)
ai_skills = ["Python", "Prompt Engineering", "Vector Databases", "LangChain"]

# 2. Accessing items (Python starts counting at 0!)
print(f"The first skill I'm learning is: {ai_skills[0]}")

# 3. Adding a new skill to the list
ai_skills.append("FastAPI")

# 4. The 'For' Loop (Like a Webflow Collection List Wrapper)
print("\n--- My AI Skill Roadmap ---")
for skill in ai_skills:
    # Everything indented here happens for EVERY skill in the list
    print(f"Target Skill: {skill}")

# 5. Counting items in a list
total_skills = len(ai_skills)
print(f"\nI have {total_skills} total skills in my roadmap.")