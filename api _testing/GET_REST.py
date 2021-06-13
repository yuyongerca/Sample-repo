
import requests
import json
# Next, we will define a variable named `url` which will contain the url needed to retrieve a list of books currently inside of the virtual library.
url = "http://localhost:8080/v1/books"
# Now, making an HTTP request is as simple as using the following line of python code.
# This will make a HTTP GET request to `http://localhost:8080/v1/books` and
# store the HTTP response in a variable called `books`.
books = requests.get(url)

# If everything went well, we can now print out the contents of the HTTP response to the screen.
# Since the virtual library API is producing Content-Type "application/json"
# We can leverage the .json() function that will transform the HTTP Response body to a Python dictionary.
print(json.dumps(books.json(), indent=4))
