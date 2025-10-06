def precision(data, theta0, theta1):
    if not data:
        return 0.0  # Avoid division by zero if data is empty

    mean_price = sum(d[1] for d in data) / len(data)
    ss_total = sum((d[1] - mean_price) ** 2 for d in data)
    ss_residual = sum((d[1] - (theta0 + theta1 * d[0])) ** 2 for d in data)

    if ss_total == 0:
        return 0.0  # Avoid division by zero if all prices are the same

    r_squared = 1 - (ss_residual / ss_total)
    return r_squared