import numpy as np
from numpy import random

sc=[1,2,4,6]
# print(sc)
total=[]
def score():
    for i in range(1,21):
        for j in range(1,7):
            f=random.choice(sc)
            total.append(f)

    # print(total)
    print(sum(total))
k=score()
#print(k)