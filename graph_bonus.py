import matplotlib.pyplot as plt
import json, utils

def plot_data(data, theta0=None, theta1=None):
    mileages = [d[0] for d in data]
    prices = [d[1] for d in data]

    plt.scatter(mileages, prices, color='blue', label='Données réelles')

    if theta0 is not None and theta1 is not None:
        min_mileage = min(mileages)
        max_mileage = max(mileages)
        x_values = [min_mileage, max_mileage]
        y_values = [theta0 + theta1 * x for x in x_values]
        plt.plot(x_values, y_values, color='red', label='Regression Model')

    plt.xlabel('Mileage (km)')
    plt.ylabel('Price (€)')
    plt.title('Distribution of Car Price Based on Mileage')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # get data
    data = utils.get_data()

    # get thetas if available
    try:
        with open('./theta.json', 'r') as file:
            theta_data = json.load(file)
        theta0 = theta_data["theta0"]
        theta1 = theta_data["theta1"]
        print(f"Using theta0={theta0}, theta1={theta1} from theta.json")
    except Exception as e:
        print(f"Error when loading theta.json: {e}. Proceeding without regression line.")
        theta0, theta1 = None, None

    # plot data
    plot_data(data)
    # plot data with regression line if thetas are available
    plot_data(data, theta0, theta1)

if __name__ == "__main__":
    main()