import csv
import random
import string

def anonymize_name(name):
    return ''.join(random.choices(string.ascii_letters, k=len(name)))

def anonymize_address(address):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=len(address)))

def anonymize_csv(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            row['first_name'] = anonymize_name(row['first_name'])
            row['last_name'] = anonymize_name(row['last_name'])
            row['address'] = anonymize_address(row['address'])
            writer.writerow(row)

if __name__ == "__main__":
    input_file = 'output.csv'
    output_file = 'output_anonymized.csv'
    anonymize_csv(input_file, output_file)
