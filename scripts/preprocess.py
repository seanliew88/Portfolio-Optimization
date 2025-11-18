import pandas as pd
import numpy as np

def proprocess_data(data):

    #Calculate the log returns
    percent_change = data.pct_change()*100
    percent_change = percent_change.round(2)
    log_return = np.log(1+percent_change)

    return log_return