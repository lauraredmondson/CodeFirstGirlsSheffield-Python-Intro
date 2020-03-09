import csv

with open('happiness_data_2016.csv', 'r') as csv_file:
    happy_data = csv.DictReader(csv_file)

    headers = happy_data.fieldnames
    print(headers)

    for country in happy_data:
        country_name = country['Country']
        region = country['Region']
        happy_rank = country['Happiness Rank']
        print('{} in {} has a happiness rank of {}'.format(country_name,region, happy_rank))
