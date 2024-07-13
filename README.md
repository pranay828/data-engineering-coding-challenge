# data-engineering-coding-challenge
This coursework project involves generating a fixed-width file, parsing it to create a delimited CSV file, and ensuring proper encoding, while adhering to basic engineering principles and testing strategies.

The project has different files as described below.

Folder Content Description

-generate_fixed_width.py: Generates random data for specified number of rows, formats it to fixed-width, and saves it to `random_data.json`.
    The output is as shown in the below image.
    
![random_json](https://github.com/user-attachments/assets/e6bc3f54-e2d8-4ebc-8888-b175731167b3)



-parse_fixed_width_file.py: Parses fixed-width data from `fixed_width.txt` and saves it as a comma separated CSV file in `output.csv`.
    The output is as shown in the below image.

    
![output_data](https://github.com/user-attachments/assets/1096d0d7-8444-43b6-8580-ccad454eb8f9)



- random_data.json: Contains original personal data including first name, last name, address, and date of birth.
    A sample of an entry is as shown below.

           {
        "first_name": "Jack",
        "last_name": "Garcia",
        "address": "241 Gotham City, St",
        "date_of_birth": "1991-09-02"
    },
  
- output.csv: Stores fixed-width formatted data generated from a JSON file with specified field lengths using parse_fixed_width_file.py file.
  
- anonymize_csv.py: Script to anonymize the first three rows of an input CSV file and save the anonymized data to a output_anonymized.csv file.

- output_anonymized.csv : CSV file with anonymized first name, last name, and address fields for the first three rows, preserving the date of birth as shown in image below.

  
![anonymized_data](https://github.com/user-attachments/assets/95478646-953d-4b7b-a7c2-dcf661a1c7d0)

<h2><b>INSTALLATION</b></h2>
To run the program in your local evironment, you begin by cloning the repository to your PC using below command.

      git clone https://github.com/pranay828/data-engineering-coding-challenge

Navgate into the newly created folder to create a virtual environment, activate it and install the required packages.

    cd data-engineering-coding-challenge

    virtualenv env

    source env/bin/activate

    pip3 install -r requirements.txt

After installation is complete, you run generate_fixed_width.py, parse_fixed_width_file.py and anonymize_csv.py in that order to get anonymized data.


<h2><b>DOCKER</b></h2>
To run the program on docker, make sure you are in your newly created folder and run below command.

    docker build -t anonymous_data_app .

