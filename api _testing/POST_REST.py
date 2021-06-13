
import requests
import json

# Next, we will define a variable named `url` which will contain the url needed to add a new book to the virtual library.
url = "http://localhost:8080/v1/books"
# Since we are ADDING a new book to the virtual library, we will need to supply some basic information on the book that our virtual library API requires. To add a book to the library, we need to supply the following.
# - The book's name, for example. "The Art of Computer Programming"
# - The author's of the book, for example. "Donald Knuth"
# - The date the book was published, for example. 1968
# - The ISBN of the book, for example. "0-201-03801-3"
# We will represent a book using a Python dictionary. We can define a variable called `book` with the following code.
book = {
    "name": "The Art of Computer Programming",
    "authors": ["Donald Knuth"],
    "date": 1968,
    "isbn": "0-201-03801-3"
}
# Now, making an HTTP POST request is as simple as using the following line of python code.
# You'll notice that we are using a `named` parameter called `json` and supplying our Python dictionary (named `book`) to this named parameter.
# When supplying the json named parameter, the requests package will automatically handle the deserialization of the dictionary
# and set the Content-Type header to application/json for you.

# This will make a HTTP POST request to http://localhost:8080/v1/books and store the HTTP response in a variable called response.
response = requests.post(url, json=book)
print(response.status_code)