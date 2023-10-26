PISTON_URL = "http://localhost:2000"
HEADERS = {"Content-Type": "application/json"}

data = {
    'language': 'py',
    'version': '3.10.0',
    'files': [{"name": "main.py", "content": ""}]
}


def setup_data_copy(filename, *args):
    d = data.copy()
    with open(filename, "r") as f:
        non_templated_data = f.read()
        d["files"][0]["content"] = non_templated_data
    return d
