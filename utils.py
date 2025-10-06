import sys, csv

def get_data():
    try:
        data = []
        with open('./data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for line in reader:
                mileage = float(line[0])
                price = float(line[1])
                data.append((mileage, price))
        return data
    except Exception as e:
        print(f"Error when loading data.csv: {e}.")
        sys.exit(1)
