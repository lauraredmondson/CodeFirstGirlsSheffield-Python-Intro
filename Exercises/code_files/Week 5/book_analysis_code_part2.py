"""Workbook for data analysis session """

import csv
# Add your imported packages here
import numpy as np

# Open the dataset
with open('book_dataset.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    # read the headers of the csv
    headers = reader.fieldnames

    # create list to store the book data
    book_data = []

    # add book data dictionaries to list from .csv
    for row in reader:
        book_data.append(row)

# display the book data list
print(book_data)

## Part 2: Introduction to numpy
# Task 2: What is the value of our current stock?



# Task 3: How much revenue did we make each month on children's books?
# 3a) Use the nested for-loop code below and adapt it to only count the revenue from children's books

revenue_months = np.zeros(6) # create an empty array of zeros to hold the revenue data
months = headers[4:] # create list with month names in from the .csv headers

for book in book_data:  # iterate through each book
    for i in range(len(months)): # iterate through each month
        revenue_months[i] += float(book['Price']) * int(book[months[i]]) # add the revenue data for each book

# 3b) Create a line graph showing the amount of revenue each month from children's books
