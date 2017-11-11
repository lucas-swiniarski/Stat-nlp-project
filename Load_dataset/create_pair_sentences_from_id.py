# -*- coding: utf-8 -*-

import pandas as pd
import json

data_file = open("data/comments.json")
data_stream = data_file.read()
data_dict = json.loads(data_stream)
print("comments dictionary loaded")

df_pair_id = pd.read_csv("data/pair_id_sentences.csv",index_col=0)
res = []
print('begin process')
for index,row in df_pair_id.iterrows():
    previous_sentence = data_dict[row['previous_sentence']]['text']
    sentence = data_dict[row['sentence']]['text']
    res.append([previous_sentence,sentence,row['label']])
    if index % 10000 ==0:
        print(index,'/',len(df_pair_id))

print('process done')

df_pair_sentence = pd.DataFrame(data=res,columns=["previous_sentence","sentence","label"])
df_pair_sentence.to_csv(path_or_buf='data/pair_sentences.csv',sep='|')

print('process saved')
