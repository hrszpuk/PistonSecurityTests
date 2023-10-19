import os
import requests

PISTON_URL = "http://localhost:2000"

# Getting list of test files
files = [file for _, _, file in os.walk(".")]
files = files[0]
files = list(filter(lambda file: file.startswith("test_") and file.endswith(".py"), files))

print(f"{len(files)} test file{'s' if len(files) > 1 else ''} found.")

# Checking connection to Piston API
try:
    test_response = requests.get(PISTON_URL)
except Exception as e:
    print(f"Unable to establish a GET request to {PISTON_URL}. Exiting.")
    exit(1)
print(f"Piston status: {test_response.status_code} (ok?: {test_response.ok})")

test_response = requests.get(PISTON_URL+"/api/v2/runtimes")
if len(test_response.json()) < 1:
    print("No runtimes found. Exiting.")
    exit(1)

print("Runtimes: ")
for runtime in test_response.json():
    print(f"- {runtime['language']} ({runtime['version']})")

# Opening file contents and building request
for filename in files:
    with open(filename, 'r') as file:
        contents = file.read()



# Sending request to Piston API and displaying the result
