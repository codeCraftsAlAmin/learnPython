# # Stack (Last In, First Out - LIFO):
books = []

books.append("JS")
books.append("PYTHON")
books.append("GO")

books.pop() # to remove

print(books)

if not books:
    print("No book left")

# # Queue (First In, First Out - FIFO):

from collections import deque


customers = deque(["x", "y", "z"])

customers.popleft() # to remove

print(customers)


if not customers:
    print("No customer left")