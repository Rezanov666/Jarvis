import csv
path = 'data/boreal_routines_2026_day1_preview.csv'

with open(path,newline="",encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
