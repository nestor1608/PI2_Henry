import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from dataset_conect import *
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

def armar_data(business):
    data = pdr.get_data_yahoo(business, start="2000-01-01")
    return data
	



