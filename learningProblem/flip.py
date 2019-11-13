import random as rd
import matplotlib.pyplot as plt
import numpy as np

def toss():
    return rd.randrange(0 , 2, 1)

def experiment():
    coins = 1000
    heads = [0]*coins
    for i in range(coins):
        for j in range(10):
            heads[i] +=  toss()
    first, minim, rand = 0, heads.index(min(heads)), rd.randrange(0, coins, 1) # Indexes of the 
    return [first, minim, rand]

if __name__ == '__main__':
    nExp = 1
    selectCoins = [0]*1000
    for i in range(nExp):
        for index in experiment():
            selectCoins[index] += 1
    print(selectCoins)
    # plt.bar(range(1000), selectCoins)
    # plt.show()