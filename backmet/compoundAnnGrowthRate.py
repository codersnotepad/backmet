def compoundAnnGrowthRate(start, end, years):

    # --- Compound Annual Growth Rate
    # start: decimal, start investment value
    # end: decimal, end investment value
    # years; int, number of years investment has been in play

    return (end / start) ** (1 / years) - 1
