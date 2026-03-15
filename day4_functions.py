# --- DAY 4: FUNCTIONS AS TOOLS ---

# 1. A tool to create a URL slug (e.g., "My Post" -> "my-post")
def create_slug(title):
    # .strip() removes outer spaces, .lower() makes it lowercase, 
    # .replace() swaps spaces for dashes
    slug = title.strip().lower().replace(" ", "-")
    return slug

# 2. A tool to check if a website image is too heavy
def check_image_size(kb_size):
    max_limit = 500  # 500kb limit for fast loading
    if kb_size > max_limit:
        return "⚠️ Warning: Image is too large! Compress it."
    else:
        return "✅ Perfect: Image is SEO friendly."

# --- TESTING OUR TOOLS ---

# Test 1: Creating a slug for a new Webflow page
page_title = "   How to Build AI Apps   "
new_url = create_slug(page_title)
print(f"Original: {page_title}")
print(f"URL Slug: www.mysite.com/{new_url}")

# Test 2: Checking a heavy hero image
hero_image_size = 1200 # 1.2MB
print(f"\nImage Scan: {check_image_size(hero_image_size)}")

# Test 3: Checking a small icon
icon_size = 45 # 45kb
print(f"Icon Scan: {check_image_size(icon_size)}")
