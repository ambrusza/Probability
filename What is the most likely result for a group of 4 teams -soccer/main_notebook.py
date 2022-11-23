#requirements
from itertools import permutations
import itertools
from itertools import combinations_with_replacement
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import time

# we have A, B, C and D teams and everyone plays everyone 1 time -> 6 matches

pairings= list(itertools.combinations(['a','b','c','d'],r=2))

print(pairings)
[('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]


#possible scoring 
# three outputs in each match - win, draw, lost (3.p vs. 0.p., 1.p vs. 1 p., 0.p. vs 3.p)
# 3**6 -- three outpot, six matches = 729 possibility

pos_scoring = [[3,0],[1,1],[0,3]]
cases = list(itertools.product(pos_scoring,repeat=6))

len(cases)
729

# final results considering all options
# the rows meaning -> points earned per team

df = pd.DataFrame()
for _x in range(len(esetek)):
    a,b,c,d =0,0,0,0
    for e,p in enumerate(esetek[_x]):
        for ex,tt in enumerate(p):
            if párosítások[e][ex] == 'a':
                a+=tt
            if párosítások[e][ex] == 'b':
                b+=tt
            if párosítások[e][ex] == 'c':
                c+=tt
            if párosítások[e][ex] == 'd':
                d+=tt

    df = pd.concat([df,pd.DataFrame({'a':a,'b':b,'c':c,'d':d}, index=[_x])])

df   
#     a	b	c	d
#   0	9	6	3	0
#   1	9	6	1	1
#   2	9	6	0	3
#   3	9	4	3	1
#   4	9	4	1	2
...	...	...	...	...
# 724	0	4	7	5
# 725	0	4	6	7
# 726	0	3	9	6
# 727	0	3	7	7
# 728	0	3	6	9

# 729 rows × 4 columns

# now comes the trick
# the points of a,b,c,d are connected row by row in descending order (the 0 should not be in front, therefore descending)

df['seq2'] = 0
for num in range(len(df)):
    jj = [str(y) for y in sorted([x for x in df.iloc[num]], reverse=True)]
    df.at[num,'seq2'] = ''.join(jj)[:-1]


