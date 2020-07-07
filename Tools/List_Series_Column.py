import pandas as pd


def series(lp, dataf):
    x = pd.Series(lp)
    dataf['column_series'] = x
