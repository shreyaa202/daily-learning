# --- DAY 10: VIRTUAL ENVIRONMENTS & PACKAGES ---

try:
    import requests
    print("✅ Success: The 'requests' library is installed in our virtual environment!")
    print(f"Library Version: {requests.__version__}")
except ImportError:
    print("❌ Error: Library not found. Did you activate the venv?")

# A small reminder of where we are
import sys
print(f"Python is running from: {sys.prefix}")