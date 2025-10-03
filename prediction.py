import sys, json

def estimate_price(mileage, theta0, theta1):
    return theta0 + (theta1 * mileage)

def main():
    if len(sys.argv) != 2:
        print("Usage: python prediction.py <given mileage>")
        return 1

    # get actual thetas
    try:
        with open('./theta.json', 'r') as file:
            data = json.load(file)
        theta = [data["theta0"], data["theta1"]]
    except Exception as e:
        print(f"Error when loading theta.json: {e}")
        sys.exit(1)

    # get estimate price
    try:
        float(sys.argv[1])
        price = estimate_price(float(sys.argv[1]), theta[0], theta[1])
        print(f"For {sys.argv[1]} miles, the price is estimated at {price:.2f}$.")
    except ValueError:
        print("The argument given is not numeric:", sys.argv[1])
        return 1

    return 0

if __name__ == "__main__":
    main()