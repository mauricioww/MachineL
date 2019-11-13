import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    x = np.linspace(-1.5, 1.5, 80)
    w1 = [1, 2, 3]
    w2 = [-1, -2, -3]
    y1 = -(w1[0]/w1[2]) - (w1[1]*x)/w1[2] 
    plot1 = plt.figure(1)
    plt.plot(x, y1, label='w = [1, 2, 3]')
    plt.title('plot 1')
    plt.legend(loc='upper left')
    plt.grid()
    plot1.show()     

    y2 = -(w2[0]/w2[2]) - (w2[1]*x)/w2[2] 
    plot2 = plt.figure(2)
    plt.plot(x, y2, label='w = -[1, 2, 3]')
    plt.title('plot 2')
    plt.legend(loc='upper left')
    plt.grid()
    plot2.show()

    input()