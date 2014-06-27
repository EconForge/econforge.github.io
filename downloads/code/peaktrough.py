"""
Authors: Chase Coleman and Spencer Lyon
Date: 06/24/2014

TODO: Add labels to the plots
"""
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.io.data import DataReader


def chopseries(data, indices, periods=40):
    """
    Takes a series and turns it into a data frame starting at each index
    and running for the number of periods specified (default is 40)
    """
    # Number or series to plot
    n = len(indices)
    c_names = ["%d cycle" % x.year for x in indices]

    new_data = pd.DataFrame(np.empty((periods, n)), columns=c_names)

    for num, date in enumerate(indices):
        date_loc = data.index.get_loc(date)
        try:
            new_data[c_names[num]] = data.ix[date_loc:date_loc+periods].values
        except:
            the_values = data.ix[date_loc:].values
            length = the_values.size
            stupiddata = np.concatenate([the_values.squeeze(),
                                        np.nan*np.ones(periods-length)])
            new_data[c_names[num]] = stupiddata

    return new_data


def peak_begin_dates(start="01/01/1972", end=datetime.now()):
    """
    Use the fred dataset `USRECQ` to determine the beginning of the
    peaks before all recessions between dates start and end
    """
    # Get quarterly recession dates from FRED
    rec_dates = DataReader("USRECQ", "fred", start=start)
    one_vals = np.where(rec_dates == 1)[0]
    rec_start = [one_vals[0]]

    # Find the beginning of the recession dates (Don't include ones that
    # begin within three years of a previous one)
    for d in one_vals:
        if d > max(rec_start) + 12:
            rec_start.append(d)

    rec_startind = rec_dates.index[rec_start]

    return rec_startind


def manhandle_freddata(fred_series, nperiods=40,
                       changetype="Percent", start="01/01/1972",
                       **plot_kwargs):
    """
    This function takes a string that corresponds to a data series from
    FRED and creates a dataframe that takes this series and creates a
    new series that shows the change of the series starting at the
    beginning of every business cycle and ending nperiods quarters later
    using either log differences or percent change.

    By default it will start at the beginning of 1972 and additionally
    data should be quarterly

    If you would like to use multiple series, use python's map function:

        map(manhandle_freddata, [list of fred_series])
    """
    # Get data
    fred_data = DataReader(fred_series, "fred", start=start)

    # Get dates for start of peak
    peak_dates = peak_begin_dates(start=start)

    # Break the time-series into chunks for each recession
    chopped_data = chopseries(fred_data, peak_dates, periods=nperiods)

    # Compute percent changes.
    if changetype.lower() == "percent":
        pct_change = ((chopped_data / chopped_data.iloc[0] - 1)*100)
    elif changetype.lower() == "log":
        logged = np.log(chopped_data)
        pct_change = (logged - logged.iloc[0]) * 100.0

    # plot data
    fig, (ax) = plt.subplots(1, 1)
    ax.set_ylabel("Percent change since previous peak")
    pct_change.index.name = "Quarters since previous peak"  # becomes x_label
    pct_change.plot(ax=ax, **plot_kwargs)
    ax.legend_.set_title(fred_series)  # set title on legend

    # add line for x-axis and show the plot.
    ax.axhline(y=0, xmin=0, xmax=nperiods, color='k', linewidth=1.5)
    plt.show()

    return pct_change


if __name__ == '__main__':
    # Get Real GDP, Real Personal Consumption, Nonresidential Investment,
    # and Output per Hour from FRED
    fred_names = ["GDPC1", "PCECC96", "GPDIC96", "OPHNFB"]

    # gdpdiff, pceccdiff, gpdicdiff, ophnfbdiff = map(manhandle_freddata,
    #                                                   fred_names)
