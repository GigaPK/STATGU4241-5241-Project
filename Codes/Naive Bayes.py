import numpy as np
import pandas as pd
from collections import defaultdict
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

# import math
# import os

names = pd.read_csv("name_gender_dataset.csv")

characters = defaultdict(int)
print(names)
character_numeric = [(' ', 0), ('a', 1), ('b', 2), ('c', 3), ('d', 4),
                     ('e', 5), ('f', 6), ('g', 7), ('h', 8), ('i', 9), ('j', 10), ('k', 11),
                     ('l', 12), ('m', 13), ('n', 14), ('o', 15), ('p', 16), ('q', 17), ('r', 18),
                     ('s', 19), ('t', 20), ('u', 21), ('v', 22), ('w', 23), ('x', 24),
                     ('y', 25), ('z', 26)]

for character, numeric in character_numeric:
    characters[character] = numeric


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

name_gender_final_df = pd.concat([names, embed_df], axis=1)
#print(name_gender_final_df)

# print(total_df.head(10))

# change genders to binary values
name_gender_final_df = name_gender_final_df.replace(["M", "F"], [0, 1])
#print(name_gender_final_df.head(10))
def neglog(x):
    return -1 * np.log(x)

# probabilities to negative log
name_gender_final_df['Neg Log Probs'] = name_gender_final_df[
    ['Probability']].apply(neglog)

#Classify Frequency as Labels
q_3=name_gender_final_df['Neg Log Probs'].quantile(0.75)
q_1=name_gender_final_df['Neg Log Probs'].quantile(0.25)
freq_label=[]
for row in name_gender_final_df['Neg Log Probs']:
    if row>=q_3:
        freq_label.append(1) #Common
    elif row<q_3 and row>=q_1:
        freq_label.append(2) #Uncommon
    else:
        freq_label.append(3) #rare

name_gender_final_df['freq_label']=freq_label
#name_gender_final_df.to_csv(r'gender_names_final.csv')


#Split test & train data
X_data=name_gender_final_df[name_gender_final_df.columns[4:31]]
X_data= X_data.drop('Neg Log Probs',1)
Y_data=name_gender_final_df[name_gender_final_df.columns[1]]
X_train, X_test, Y_train, Y_test = train_test_split(X_data,Y_data,test_size=0.33,random_state=42)

#Create NaiveBayes Model
model=GaussianNB()
model.fit(X_train,Y_train)
model_score = model.score(X_test,Y_test)
print(model_score)
