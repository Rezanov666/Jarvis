import csv
from itertools import islice
path = 'data/boreal_routines_2026_day1_preview.csv'
print("Andrii Riezanov")
with open(path,newline="",encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in islice(reader, 3):
        print(row)
