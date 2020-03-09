import csv

with open('crime_data_san_fran_2018.csv', 'r') as csv_file:
    crime_data = csv.DictReader(csv_file)

    headers = crime_data.fieldnames
    print(headers)

    for crime in crime_data:
        crime_type = crime['Category']
        day= crime['Day']
        region = crime['District']
        outcome = crime['Resolution']
        print('Crime: {}, Day: {}, Area: {}, Resolution: {}'.format(crime_type, day, region, outcome))