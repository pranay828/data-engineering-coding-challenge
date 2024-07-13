import random
from datetime import datetime, timedelta
import json
import os

# specifications 
spec = [
    ("first_name", 10),
    ("last_name", 10),
    ("address", 20),
    ("date_of_birth", 10)
]

# data for names and cities
first_names = ["Alice", "Bob", "Charlie", "David", "Emily", "Frank", "Grace", "Henry", "Isabella", "Jack"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
cities = ["Springfield", "Shelbyville", "Capital City", "Hill Valley", "Smalltown", "Riverdale", "Gotham City"]

#  generate a random date of birth between two dates
def random_date_of_birth(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

def generate_random_data(rows):
    data = []
    start_date = datetime(1950, 1, 1)
    end_date = datetime(2005, 12, 31)

    for _ in range(rows):
        first_name = random.choice(first_names).ljust(spec[0][1]) 
        last_name = random.choice(last_names).ljust(spec[1][1])  
        address = f"{random.randint(1, 999)} {random.choice(cities)}, {random.choice(['St', 'Ave', 'Blvd'])}".ljust(spec[2][1]) 
        date_of_birth = random_date_of_birth(start_date, end_date).strftime('%Y-%m-%d').ljust(spec[3][1])  
        data.append({
            "first_name": first_name.strip(),   
            "last_name": last_name.strip(),    
            "address": address.strip(),          
            "date_of_birth": date_of_birth.strip()  
        })
    
    return data

if __name__ == "__main__":
    num_rows = 50000  
    random_data = generate_random_data(num_rows)

    file_path = 'random_data.json'
    print(f"Saving data to: {os.path.abspath(file_path)}")

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(random_data, f, ensure_ascii=False, indent=4)
        
        print("Data has been saved to random_data.json.")
    
    except Exception as e:
        print(f"Error saving data: {e}")
