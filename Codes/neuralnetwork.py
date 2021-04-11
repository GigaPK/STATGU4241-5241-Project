#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
#os.getcwd()
# os.chdir('/Users/yunjeesun/Documents/GitHub/STATGU4241-5241-Project/')
 ## i am commenting this out becasue this indicates working directory


import torch
import random
from torch.utils.data import TensorDataset, DataLoader
from torch import optim
import torch.nn as nn
import torch.nn.functional as P
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


data = pd.read_csv("gender_names_final.csv")
data_y = data["Neg Log Probs"]
data_x = data[["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
              "11", "12", "13", "14", "15", "16", "17", "18", "19",
              "20", "21", "22", "23", "24"]]

