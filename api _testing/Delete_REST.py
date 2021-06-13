
import requests
import json
url = "http://localhost:8080/v1/books"
book = {
    "name": "The Art of Computer Programming",
    "authors": [
    "Donald Knuth"
    ],
    "date": 1968,
    "isbn": "0-201-03801-3"
}

# Add the Book
response = requests.post(url, json=book)
book_data = response.json()


# Let's now delete the book that we just added to the library.
delete_book_url = "http://localhost:8080/v1/books/{}".format(book_data['uuid'])
response = requests.delete(delete_book_url)

print("http status code after deleting the book: ", response.status_code)
