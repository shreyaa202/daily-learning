# --- DAY 6: ERROR HANDLING (TRY/EXCEPT) ---

def safe_divide(number, divisor):
    try:
        # Try to do the math
        result = number / divisor
        return f"Result: {result}"
    except ZeroDivisionError:
        # What to do if the user tries to divide by 0
        return "❌ Error: You cannot divide by zero!"
    except TypeError:
        # What to do if the user enters text instead of a number
        return "❌ Error: Please provide numbers only."

# --- TESTING ---

print(safe_divide(10, 2))   # Works fine
print(safe_divide(10, 0))   # Catches the ZeroDivisionError
print(safe_divide(10, "A")) # Catches the TypeError