import numpy as np
import matplotlib.pyplot as plt

def simulate(ncoin, ntoss):
    outcome = np.random.choice((0., 1.), size=(ncoin, ntoss))
    heads = np.sum(outcome, axis=1)
    heads /= 10
    return heads[0], np.random.choice(heads), np.min(heads)

def plott1():
    bins = np.linspace(0, 1, 22)
    f1 = plt.figure(1)
    plt.hist(experiments[:, 0], bins, alpha=0.5, label="first one")
    plt.hist(experiments[:, 1], bins, alpha=0.5, label="random")
    plt.hist(experiments[:, 2], bins, alpha=0.5, label="minimun")
    plt.legend()
    f1.show()

def P(outcomes, mu, epsilon):
    less = np.sum(outcomes < mu - epsilon)
    greater = np.sum(outcomes > mu + epsilon)
    return (less + greater) / len(outcomes)

def hoeffding(epsilon, N):
    return 2 * np.exp(-2 * epsilon * epsilon * N)

def plott2():
    epsilons = np.linspace(0, 1, 100)
    P_first = [P(experiments[:, 0], mu, epsilon) for epsilon in epsilons]
    P_random = [P(experiments[:, 1], mu, epsilon) for epsilon in epsilons]
    P_min = [P(experiments[:, 2], mu, epsilon) for epsilon in epsilons]
    P_hoeffding = [hoeffding(epsilon, ntoss) for epsilon in epsilons]
    f2 = plt.figure(2)
    plt.plot(epsilons, P_first, label="first")
    plt.plot(epsilons, P_random, label="random")
    plt.plot(epsilons, P_min, label="min")
    plt.plot(epsilons, P_hoeffding, label="Hoeffding")
    plt.legend()
    # plt.show()
    f2.show()

if __name__ == '__main__':
    ncoin = 1000 # Number of fair coins for each experiment
    ntoss = 10 # Number of toss for each coin
    mu = 0.5 # Probability
    nexperiment = 100000 # Number of experiments
    experiments = np.empty((nexperiment, 3))
    for i in range(nexperiment):
        first, rand, minimun = simulate(ncoin, ntoss)
        experiments[i, 0], experiments[i, 1], experiments[i, 2] = first, rand, minimun
    plott1()
    plott2()
    c = input()