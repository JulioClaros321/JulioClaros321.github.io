import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import  ARIMA

def main():

    shampoo = pd.read_csv("shampoo_with_exog .csv", index_col= [0], parse_dates=True, squeeze=True)


    shampoo_base = pd.concat([shampoo, shampoo.shift(1)], axis=1)

    shampoo_base.columns = ["Actual_Sales", "Forecast_Sales"]
    shampoo_base.dropna(inplace=True)
    #print(shampoo_base.head())
    #shampoo.ma = shampoo.rolling(window=10).mean()

    shampoo_error = mean_squared_error(shampoo_base.Actual_Sales, shampoo_base.Forecast_Sales)
    np.sqrt(shampoo_error)

    print(np.sqrt(shampoo_error))

    #plot_acf(shampoo)
    # Q - 3

    #plot_pacf(shampoo)
    # P - 2

    #D - 0-2

    shampoo.train

    plt.show()

if __name__ == '__main__':
    main()