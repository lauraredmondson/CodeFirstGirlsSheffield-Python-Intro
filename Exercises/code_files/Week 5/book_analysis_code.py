"""Workbook for data analysis session """

import csv
# Add your imported packages here


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

# display the book data for the first book
print(book_data[0])

# PART 1: Data analysis

# %%[Task 1: Calculating the number of books in each Genre]
# Create an empty list called book_genres

# 1a) Write a for loop and append each Genre to the list

# 1b) Use the counter method to calculate the number of books in each genre

# 1c) Plot the number of books in each genre, remember to add the import statement to the top of your file.
