# Fill in this file with the code from the course introducti
import requests
import jason
r = requests.get("https://github.com")
print (r.status_code)
print(json.dumps(r.json(), indent = 4))