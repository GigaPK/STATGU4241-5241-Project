#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 17:16:37 2021

@author: Philip
"""
import numpy as np
import pandas as pd
from collections import defaultdict
# import math

names = pd.read_csv("name_gender_dataset.csv")

characters = defaultdict(int)

character_numeric = [(' ', 0), ('a', 1),('b', 2), ('c', 3), ('d', 4),
('e', 5), ('f', 6), ('g', 7), ('h', 8), ('i', 9), ('j', 10), ('k', 11),
('l', 12), ('m', 13), ('n', 14), ('o', 15),('p', 16), ('q', 17), ('r', 18),
('s', 19), ('t', 20), ('u', 21), ('v', 22),('w', 23), ('x', 24), 
('y', 25), ('z', 26)]

for character, numeric in character_numeric: 
    characters[character]=numeric
    
# ndarray
name_array = np.array(names.Name)
total_name_array = []
for name in name_array: 
    char_array = np.zeros(25)
    for idx, char in enumerate(name.lower()):
        char_idx = characters[char]
        char_array[idx] = char_idx
    total_name_array.append(char_array)

embed_df = pd.DataFrame(total_name_array)

name_gender_final_df = pd.concat([names, embed_df], axis = 1)
#print(total_df.head(10))

# probabilities to negative log
def neglog(x): 
    return -1*np.log(x)

name_gender_final_df['Neg Log Probs'] = name_gender_final_df[
    ['Probability']].apply(neglog)

print(name_gender_final_df.head(10))

name_gender_final_df.to_csv(r'/Users/philip/Stat_ML/Project/STATGU4241-5241-Project/data_processing/gender_names_final.csv')







