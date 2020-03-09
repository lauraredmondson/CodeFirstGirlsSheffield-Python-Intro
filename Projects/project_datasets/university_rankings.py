import csv

with open('university_rankings.csv', 'r') as csv_file:
    uni_data = csv.DictReader(csv_file)

    headers = uni_data.fieldnames
    print(headers)

    for university in uni_data:
        institution = university['institution']
        rank = university['rank_2020']
        country = university['country']
        print('Institution: {}, Rank: {}, Country: {}'.format(institution, rank, country))
