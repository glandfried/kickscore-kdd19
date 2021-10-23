import matplotlib.pyplot as plt
import numpy as np
import os
import pickle
import psutil
import time 

from datetime import datetime
from kseval.models import basketball, tennis
from kseval.plotting import sigconf_settings
from kseval.utils import data_path
from kseval.models.base import iterate_dataset
from matplotlib.dates import YearLocator, DateFormatter

from math import log, exp

N = 0
for obs in iterate_dataset("../data/kdd-tennis.txt"):
    N += 1 

m_start = psutil.virtual_memory().available; start = time.time()

model = tennis.AffineWienerModel(ovar=0.36622,wvar=0.14782,svar=0.001)
model.fit_params["max_iter"] = 10
model.fit()
exp(model.ks_model.log_likelihood/N) # 0.54593

elapsed = time.time() - start; m_epased = m_start - psutil.virtual_memory().available


with open("../replicate.log", "w") as text_file:
    text_file.write("dataset, rate, time, memory\n")
    text_file.write("tennis, {}, {}, {}\n".format(rate, elapsed, m_epased/(1024.0 ** 3)))
