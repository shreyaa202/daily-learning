# --- DAY 7: MODULES (USING LIBRARIES) ---

# 1. Importing built-in modules
import random
import datetime

# 2. Using the 'datetime' module
current_time = datetime.datetime.now()
print(f"Project Started at: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

# 3. Using the 'random' module (Great for AI variations)
ai_responses = [
    "I can help with that!",
    "That's an interesting question.",
    "Let me look that up for you.",
    "I'm not sure, but here is what I found."
]

random_reply = random.choice(ai_responses)
print(f"AI Assistant says: {random_reply}")

# 4. A quick math module example
import math
print(f"The square root of 64 is: {math.sqrt(64)}")