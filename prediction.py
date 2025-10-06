import sys, utils

def estimate_price(mileage, theta0, theta1):
    return theta0 + (theta1 * mileage)

def main():
    if len(sys.argv) != 2:
        print("Usage: python prediction.py <given mileage>")
        return 1

    # get actual thetas
    theta0, theta1 = utils.get_thetas()
    if theta0 is None or theta1 is None:
        print("Theta values not found. Please run the training script first.")
        return 1

    # get estimate price
    try:
        float(sys.argv[1])
        price = estimate_price(float(sys.argv[1]), theta0, theta1)
        print(f"For {sys.argv[1]} miles, the price is estimated at {price:.2f}$.")
    except ValueError:
        print("The argument given is not numeric:", sys.argv[1])
        return 1

    return 0

if __name__ == "__main__":
    main()