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
for _x in range(len(cases)):
    a,b,c,d =0,0,0,0
    for e,p in enumerate(cases[_x]):
        for ex,tt in enumerate(p):
            if pairings[e][ex] == 'a':
                a+=tt
            if pairings[e][ex] == 'b':
                b+=tt
            if pairings[e][ex] == 'c':
                c+=tt
            if pairings[e][ex] == 'd':
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

#       a	b	c	d	seq2
#   0   9	6	3	0	9630
#   1	9	6	1	1	9611
#   2	9	6	0	3	9630
#   3	9	4	3	1	9431
#   4	9	4	1	2	9421
# ...	...	...	...	...	...
# 724	0	4	7	5	7540
# 725	0	4	6	7	7640
# 726	0	3	9	6	9630
# 727	0	3	7	7	7730
# 728	0	3	6	9	9630

# 729 rows × 5 columns

#we aggregate the results according to the cases

df_cases = pd.DataFrame(df.groupby('seq2').size().sort_values(ascending=False)).reset_index().rename(columns={0:'sum'})

df_cases.head(

# 	seq2	sum
# 0	7441	36
# 1	6443	36
# 2	7422	24
# 3	6633	24
# 4	9431	24

#it can be seen that 7441 and 6443 are the most common results -> 36 and 36
    
# finally we calculate their probabilities -> number of successful outcomes/number of possible outcomes
    
d_cases['p'] = d_cases['sum']/sum(d_cases['sum'])
d_cases

#   seq2	sum	p
#   0	7441	36	0.049383
#   1	6443	36	0.049383
#   2	7422	24	0.032922
#   3	6633	24	0.032922
#   4	9431	24	0.032922
#   5	9421	24	0.032922
#   6	7640	24	0.032922
#   7	7631	24	0.032922
#   8	7621	24	0.032922
#   9	7540	24	0.032922
# 10	7531	24	0.032922
# 11	7521	24	0.032922
# 12	7433	24	0.032922
# 13	7432	24	0.032922
# 14	7431	24	0.032922
# 15	6641	24	0.032922
# 16	9630	24	0.032922
# 17	6541	24	0.032922
# 18	6442	24	0.032922
# 19	5432	24	0.032922
# 20	5442	24	0.032922
# 21	5541	24	0.032922
# 22	5443	24	0.032922
# 23	9440	12	0.016461
# 24	5532	12	0.016461
# 25	5531	12	0.016461
# 26	5522	12	0.016461
# 27	7322	12	0.016461
# 28	6522	12	0.016461
# 29	7730	12	0.016461
# 30	9611	12	0.016461
# 31	5332	12	0.016461
# 32	6660	8	0.010974
# 33	4443	8	0.010974
# 34	9333	8	0.010974
# 35	7711	6	0.008230
# 36	4444	6	0.008230
# 37	5550	4	0.005487
# 38	9222	4	0.005487
# 39	3333	1	0.001372

# it can be seen that the probability of the two results is about 5%
# so that everyone has 3 points and the smallest one -> 0.1%
