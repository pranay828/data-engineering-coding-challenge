import csv
import json

def parse_json_to_csv(input_file, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['first_name', 'last_name', 'address', 'date_of_birth'])  

        with open(input_file, 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)

            for record in data:
                first_name = record.get('first_name', '').strip()
                last_name = record.get('last_name', '').strip()
                address = record.get('address', '').strip()
                date_of_birth = record.get('date_of_birth', '').strip()

                writer.writerow([first_name, last_name, address, date_of_birth])

if __name__ == "__main__":
    input_file = 'random_data.json'
    output_file = 'output.csv'

    parse_json_to_csv(input_file, output_file)
    print(f"Data has been parsed from {input_file} and saved to {output_file}.")
