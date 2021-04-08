 import os
 os.getcwd()
# os.chdir('/Users/yunjeesun/Documents/GitHub/STATGU4241-5241-Project/')
 ## i am commenting this out becasue this indicates working directory


from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


data = pd.read_csv("dataset/gender_names_final.csv")
 data.head()

