# Description: Short example for Identifying and Correcting for Serial Correlation in Dynamic Models for Time Series.


import logging
from datetime import datetime

import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.graphics.tsaplots as tsaplots
from pandas_datareader import data as web
from statsmodels.regression.linear_model import GLS, GLSAR
from statsmodels.stats.diagnostic import acorr_breusch_godfrey

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)


# Function to fetch data from FRED
def get_fred_data(series_id, start_date="2000-01-01", end_date=None):
    if end_date is None:
        end_date = datetime.now().strftime("%Y-%m-%d")
    df = web.DataReader(series_id, "fred", start_date, end_date)
    return df.dropna()



def main():
    # Fetch University of Michigan Consumer Sentiment Index (MICH)
    series_id = "MICH"
    mich_data = get_fred_data(series_id)
    mich_data = mich_data.pct_change().dropna()  # Convert to percentage change

    # Prepare DataFrame
    mich_data = mich_data.rename(columns={series_id: "MICH"})
    mich_data["Date"] = mich_data.index  # Ensure a date column for plotting

    # Create lagged MICH values
    for lag in range(1, 3):  # Include 2 lags
        mich_data[f"MICH_lag{lag}"] = mich_data["MICH"].shift(lag)

    # Drop missing values due to lagging
    mich_data.dropna(inplace=True)

    # Define independent and dependent variables
    X_lags = ["MICH", "MICH_lag1", "MICH_lag2"]
    X_matrix = sm.add_constant(mich_data[X_lags])  # Add intercept
    y_vector = mich_data["MICH"]  # Target is MICH itself (can be changed)

    # Fit a distributed lag model
    model = sm.OLS(y_vector, X_matrix).fit()

    # Perform the Breusch-Godfrey test for serial correlation
    bg_test = acorr_breusch_godfrey(model, nlags=2)

    logger.info(f"Breusch-Godfrey Test p-value: {bg_test[1]:.4f}")

    gls_model = GLS(y_vector, X_matrix).fit()
    logger.info(gls_model.summary())

    cochrane_orcutt = GLSAR(y_vector, X_matrix, rho=1).iterative_fit()
    logger.info(cochrane_orcutt.summary())

    model_robust = model.get_robustcov_results(cov_type="HAC", maxlags=2)
    logger.info(model_robust.summary())

    # Extract residuals
    residuals = model.resid
    # Plot ACF
    plt.figure(figsize=(10, 5))
    tsaplots.plot_acf(residuals, lags=20, alpha=0.05)
    plt.xlabel("Lag")
    plt.ylabel("Autocorrelation")
    plt.title("Autocorrelation of Residuals")
    plt.savefig("residual_acf.png")
    plt.show()


if __name__ == "__main__":
    main()
