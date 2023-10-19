import os
import requests

PISTON_URL = "http://localhost:2000"

# Getting list of test files
files = [file for _, _, file in os.walk(".")]
files = files[0]
files = list(filter(lambda file: file.startswith("test_") and file.endswith(".py"), files))

print(f"{len(files)} test file{'s' if len(files) > 1 else ''} found.")

# Checking connection to Piston API
test_response = requests.get(PISTON_URL)
print(f"Piston status: {test_response.status_code} (ok?: {test_response.ok})")

test_response = requests.get(PISTON_URL+"/api/v2/runtimes")
print(test_response.json())

# Opening file contents and building request


# Sending request to Piston API and displaying the result
