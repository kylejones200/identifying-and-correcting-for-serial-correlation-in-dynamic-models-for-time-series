# Identifying and Correcting for Serial Correlation in Dynamic Models for Time Series

Published: 2025-03-08
Medium: [https://medium.com/@kyle-t-jones/identifying-and-correcting-for-serial-correlation-in-dynamic-models-for-time-series-afffeeacbde2](https://medium.com/@kyle-t-jones/identifying-and-correcting-for-serial-correlation-in-dynamic-models-for-time-series-afffeeacbde2)

## Business context

Dynamic models in time series often exhibit serial correlation, a condition where error terms are correlated across time. Serial correlation violates the classical assumption of independent errors, leading to inefficient estimates, incorrect standard errors, and misleading statistical inferences.

Serial correlation, also known as autocorrelation, occurs when the residuals (ϵt) of a regression model are correlated with past residuals (ϵt−1,ϵt−2,...). In dynamic models, where past values of variables influence the present, serial correlation is a common issue.

- ϵt is the error term at time t. - k is the lag order. - If ρ>0, we have positive serial correlation (errors move together in the same direction). - If ρ<0, we have negative serial correlation (errors alternate in sign).

## About

Place the code for this article in this repository.
The original article export is saved as `article.md`.

## Files

Add your `.ipynb`, `.py`, `.yaml`, `.js`, `.ts`, or other project files here.

## Disclaimer

Educational/demo code only. Not financial, safety, or engineering advice. Use at your own risk. Verify results independently before any production or operational use.

## License

MIT — see [LICENSE](LICENSE).