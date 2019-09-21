#!/usr/bin/python3.4
"""reducer.py"""

import sys
import csv
from collections import OrderedDict

from collections import Counter
import pandas as pd
word2count={}

current_word = []
current_count = []

for line in sys.stdin:
    line =line.strip()
    word,count=line.split('\t',1)
    
    try:
        count =int(count)
    except ValueError:
        continue
    
    try:
        word2count[word]=word2count[word]+count
    except:
        word2count[word]=count



top_ten = dict(Counter(word2count).most_common(10))
df = pd.DataFrame([[key,value] for key,value in top_ten.items()],columns=["name","count"])
df.sort_values(by = ['count'], ascending = False, inplace = True)

current_word=df['name']
current_count=df['count']

for i in range(len(current_word)):
	print('%s\t%s' % (current_word[i],current_count[i]))
#df.to_csv('twitter_norm.csv',sep=',',encoding='utf-8',index=False)
#df1 = pd.read_csv('data_reduce.csv', sep=',', encoding='utf-8')

#print(df1)
