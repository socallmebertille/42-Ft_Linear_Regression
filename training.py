import sys, json, csv, prediction

def get_theta():
    try:
        with open('./theta.json', 'r') as file:
            data = json.load(file)
        theta = [data["theta0"], data["theta1"]]
        return theta[0], theta[1]
    except Exception as e:
        print(f"Error when loading theta.json: {e}")
        sys.exit(1)

def gradient_descent_algorithm(data, theta0, theta1, learningRate=0.07):
    sum = 0
    for elem in data:
        sum += prediction.estimate_price(elem[0], theta0, theta1) - elem[1]
    tmp0 = learningRate * (sum/len(data)) if len(data) > 0 else None
    theta0 -= tmp0
    sum = 0
    for elem in data:
        sum += (prediction.estimate_price(elem[0], theta0, theta1) - elem[1]) * elem[0]
    tmp1 = learningRate * (sum/len(data)) if len(data) > 0 else None
    theta1 -= tmp1
    return theta0, theta1

def main():
    # get data
    try:
        data = []
        with open('./data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader) # skip header
            for line in reader:
                mileage = float(line[0])
                price = float(line[1])
                data.append((mileage, price))
    except Exception as e:
        print(f"Error when loading data.csv: {e}.")
        sys.exit(1)

    # get actual thetas
    theta0, theta1 = get_theta()
    print(f"Old thetas: {theta0:.2f} {theta1:.2f}")

    # update thetas's values
    theta0, theta1 = gradient_descent_algorithm(data, theta0, theta1)
    print(f"New thetas: {theta0:.2f} {theta1:.2f}")

    # update theta.json
    try:
        with open('./theta.json', 'w') as file:
            json.dump({"theta0": theta0, "theta1": theta1}, file)
    except Exception as e:
        print(f"Error when saving theta.json: {e}.")
        sys.exit(1)

    return 0

if __name__ == "__main__":
    main()