def maxDrawDown(returns, dates, printGraph=False):

    # --- Maximum Draw Down
    # returns: array, cumulative returns by period (e.g day) of investment
    # dates: array, dates associated with the returns
    # printGraph: boolean, will print graph and summary details

    import numpy as np

    # --- get first non nan index
    for i in range(len(returns)):

        if np.isnan(returns[i]) == False:

            firstNonNan = i
            break

    # --- get last non nan index
    for i in reversed(range(len(returns))):

        if np.isnan(returns[i]) == False:

            lastNonNan = i
            break

    # --- replace nans with zeros
    for i in range(len(returns)):

        if i < firstNonNan:
            returns[i] = 0

        elif i > lastNonNan:
            returns[i] = 0

    end = np.argmax(np.maximum.accumulate(returns) - returns)  # end of the period
    start = np.argmax(returns[:end])  # start of period

    mdd = returns[start] - returns[end]

    if printGraph:

        import matplotlib.pyplot as plt

        plt.plot(dates, returns)
        plt.axvspan(dates[start], dates[end], color="red", alpha=0.1)
        plt.show()

        print("Start:     ", dates[start])
        print("End:       ", dates[end])
        print("Duration:  ", dates[end] - dates[start])
        print("MMD:       ", round(mmd, 2))

    # outputs
    # mdd: decimal, max draw down value
    # dates[start]: date, when mdd started
    # dates[end]: date, when mdd ended

    return mdd, dates[start], dates[end]
