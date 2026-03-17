import json

# 1. Simulating a 'JSON' response from an AI Model
# (In real life, this would come from an API)
ai_response_json = '''
{
    "model": "gpt-4-ai",
    "usage": {
        "prompt_tokens": 50,
        "completion_tokens": 120
    },
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "Hello Shreya! I am ready to help you build your AI app."
            },
            "finish_reason": "stop"
        }
    ]
}
'''

# 2. Parsing the JSON (Turning the string into a Python Dictionary)
data = json.loads(ai_response_json)

# 3. Digging for specific data
# To get the content, we have to go: data -> choices -> first item [0] -> message -> content
message_content = data['choices'][0]['message']['content']
token_count = data['usage']['completion_tokens']

print("--- 🤖 AI Data Extraction ---")
print(f"AI Said: {message_content}")
print(f"Tokens Used: {token_count}")

# 4. Bonus: Making it look pretty (Perfect for debugging)
print("\n--- Pretty Printed JSON ---")
print(json.dumps(data, indent=4))