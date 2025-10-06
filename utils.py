import sys, csv, json

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

def get_thetas():
    try:
        with open('./theta.json', 'r') as file:
            data = json.load(file)
        theta0 = data["theta0"]
        theta1 = data["theta1"]
        print(f"(θ0, θ1) = ({theta0:.4f}, {theta1:.4f})")
        return theta0, theta1
    except Exception as e:
        print(f"Error when loading theta.json: {e}. Proceeding without regression line.")
        return None, None