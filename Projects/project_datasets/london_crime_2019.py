import csv

with open('crime_data_london_2019.csv', 'r') as csv_file:
    crime_data = csv.DictReader(csv_file)

    headers = crime_data.fieldnames
    print(headers)

    for crime in crime_data:
        crime_type = crime['Crime_type']
        region = crime['Area']
        outcome = crime['Outcome']
        print('Crime: {}, Area: {}, Resolution: {}'.format(crime_type,region, outcome))
