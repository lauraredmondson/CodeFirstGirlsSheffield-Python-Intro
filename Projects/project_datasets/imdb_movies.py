import csv

with open('IMDB_data.csv', 'r') as csv_file:
    movie_data = csv.DictReader(csv_file)

    headers = movie_data.fieldnames
    print(headers)

    for movie in movie_data:
        title = movie['Title']
        rating = movie['Rating']
        print('{} has a rating of {} on IMDb'.format(title, rating))
