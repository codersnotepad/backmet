def sharpeRatio(returns, periods, rf=0):

    # --- Annualised Sharpe Ratio
    # returns: array, percentage change values in decimals
    # periods: int, annual periods in returns (e.g. days = 252, months = 12)
    # rf: decimal, Risk Free Rate generally zero but can be specified as a decimal

    import numpy as np

    sr = np.sqrt(periods) * ((np.nanmean(returns) - rf) / np.nanstd(returns))

    # --- if value is +-inf then set to Nan
    if sr == np.inf or sr == -np.inf:
        sr = np.nan

    return sr
