# This writes all columns to the files. So don't delete or add unnecessary ones in the csv.
import csv

with open('provinces.csv', 'r', encoding='ANSI') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')
    for row in reader:
        province_id = row['provinceId']
        province_name = row['provinceName']
        filename = f"{province_id} - {province_name}.txt"
        with open(filename, 'w', encoding='utf-8') as output_file:
            for column, value in row.items():
                if column not in ['provinceId', 'provinceName']:
                    output_file.write(f"{column} = {value}\n")
                if column in ['capital', 'provinceName']:
                    output_file.write(f"{column} = \"{value}\"\n")
print("Files created successfully.")
