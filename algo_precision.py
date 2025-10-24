import utils


def precision(data, theta0, theta1):
    if not data:
        return 0.0  # Avoid division by zero if data is empty

    mean_price = sum(elem[1] for elem in data) / len(data)

    # Total sum of squares = total variance of data = Σ(y_i - ȳ)²
    ss_total = sum((elem[1] - mean_price) ** 2 for elem in data)

    # Residual sum of squares = errors = Σ(y_i - ŷ_i)²
    ss_residual = sum(
        (elem[1] - (theta0 + theta1 * elem[0])) ** 2 for elem in data
    )

    rmse = (ss_residual / len(data)) ** 0.5  # Root Mean Squared Error

    # R² = 1 - (Σ(y_i - ŷ_i)² / Σ(y_i - ȳ)²)
    return 1 - (ss_residual / ss_total) if ss_total != 0 else 0.0, rmse


def main():
    # get data
    data = utils.get_data()
    # get thetas if available
    theta0, theta1 = utils.get_thetas()
    if theta0 is None or theta1 is None:
        print("Theta values not found. Please run the training script first.")
        return 1

    r_squared, rmse = precision(data, theta0, theta1)
    print(f"R² (coefficient of determination): {r_squared:.4f}")
    if r_squared >= 0.9:
        print("=> The model is considered very precise.")
    elif r_squared >= 0.7:
        print("=> The model is considered good.")
    elif r_squared >= 0.5:
        print("=> The model could be improved.")
    else:
        print("=> The model is not very good.")
    print(f"Average error : ±{rmse:.0f}€")

    return 0


if __name__ == "__main__":
    main()
