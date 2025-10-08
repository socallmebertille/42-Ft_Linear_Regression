import sys, json, prediction, utils

def calculate_thetas(data, theta0, theta1, learningRate):
    sum0 = 0
    sum1 = 0
    for elem in data:
        error = prediction.estimate_price(elem[0], theta0, theta1) - elem[1]
        sum0 += error
        sum1 += error * elem[0]
    
    tmp0 = learningRate * (sum0/len(data)) if len(data) > 0 else 0
    tmp1 = learningRate * (sum1/len(data)) if len(data) > 0 else 0
    
    theta0 -= tmp0
    theta1 -= tmp1
    return theta0, theta1

def gradient_descent_algorithm(data):
    theta0, theta1, learningRate = 0.0, 0.0, 0.1
    i, iterations = 0, 1000
    converged = False
    threshold = 0.0001

    while not converged and i < iterations:
        old_theta0, old_theta1 = theta0, theta1
        theta0, theta1 = calculate_thetas(
            data, theta0, theta1, learningRate
        )
        change = abs(theta0 - old_theta0) + abs(theta1 - old_theta1)
        if change < threshold:
            print(f"\n✅ Convergence achieved at iteration {i} (change={change:.6f})")
            converged = True
    return theta0, theta1

def main():
    # get data
    data = utils.get_data()
    
    # STEP 1 : get min & max to normalize data
    mileages = [d[0] for d in data]
    prices = [d[1] for d in data]
    
    min_mileage = min(mileages)
    max_mileage = max(mileages)
    min_price = min(prices)
    max_price = max(prices)
    
    print(f"\nMileage range: {min_mileage} - {max_mileage} km")
    print(f"Price range: {min_price} - {max_price} €")
    
    # STEP 2 : normalize data between 0 and 1
    # formula : value_normalized = (value - min) / (max - min)
    normalized_data = []
    for mileage, price in data:
        norm_mileage = (mileage - min_mileage) / (max_mileage - min_mileage)
        norm_price = (price - min_price) / (max_price - min_price)
        normalized_data.append((norm_mileage, norm_price))
    
    print("\nExample:")
    print(f"Before: {data[0][0]} km, {data[0][1]}€")
    print(f"After: {normalized_data[0][0]:.4f}, {normalized_data[0][1]:.4f}")

    # STEP 3 : gradient descend algorithm (= train on normalized data)
    theta0, theta1 = gradient_descent_algorithm(normalized_data)
    
    # STEP 4 : denormalize thetas
    # formula to get back real thetas : value = value_normalized * (max - min) + min
    real_theta1 = theta1 * (max_price - min_price) / (max_mileage - min_mileage)
    real_theta0 = min_price + theta0 * (max_price - min_price) - real_theta1 * min_mileage
    
    print(f"\nFinal thetas : theta0={real_theta0:.2f}, theta1={real_theta1:.6f}")

    # verification
    print("\nCheck predictions:")
    for i in [0, len(data)//2, -1]:
        km = data[i][0]
        real_price = data[i][1]
        predicted = real_theta0 + real_theta1 * km
        print(f"{km:6.0f} km: real={real_price}€, predicted={predicted:.0f}€")
    
    # save thetas in json (a & b from y = ax + b)
    try:
        with open('./theta.json', 'w') as file:
            json.dump({"theta0": real_theta0, "theta1": real_theta1}, file)
        print("\nThetas saved to theta.json ✅")
    except Exception as e:
        print(f"Error when saving theta.json: {e}.")
        sys.exit(1)

    return 0

if __name__ == "__main__":
    main()
