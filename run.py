import os
import requests
import json

PISTON_URL = "http://localhost:2000"
HEADERS = {"Content-Type": "application/json"}

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

test_response = requests.get(PISTON_URL + "/api/v2/runtimes")
if len(test_response.json()) < 1:
    print("No runtimes found. Exiting.")
    exit(1)

print("Runtimes: ")
for runtime in test_response.json():
    print(f"- {runtime['language']} ({runtime['version']})")

data = {'language': 'py', 'version': '3.10.0', 'files': [{}]}

# Opening file contents and building request
for filename in files:
    with open(filename, 'r') as file:
        contents = file.read()
        data['files'][0]['name'] = filename
        data['files'][0]['content'] = contents
        print(f"Running \"{filename}\"...")
        response = requests.post(PISTON_URL + "/api/v2/execute", json=data, headers=HEADERS)
        try:
            print(f"Finished: {response.json()['run']}")
        except KeyError as e:
            print(f"Run failed: {response.json}")

# Sending request to Piston API and displaying the result
