import csv
from fastapi import FastAPI

app = FastAPI()

# Function to read the CSV file and parse its data
def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Path to the CSV file
file_path = r'C:\Users\bhars\Downloads\smalldb_134.csv'

# Read the CSV file and parse its data
csv_data = read_csv(file_path)

# API endpoint to retrieve all data
@app.get('/api/data')
def get_all_data():
    return csv_data

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
