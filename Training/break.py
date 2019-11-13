def printOne_D(pattern):
    listt = list(pattern)
    print(str.join('\t', listt))

def printTwo_D(pattern):
    print("%s\t%s" % (pattern[0], pattern[1]))
    print("%s\t%s" % (pattern[2], pattern[3]))


binaries = lambda x, n: format(x, 'b').zfill(n) # For 2D perceptron

if __name__ == '__main__':
    for i in range(16):
        bin_ = binaries(i, 4)
        printTwo_D(bin_)
        print("-"*20)

    print('*'*30)

    for j in range(2, 4, 1):
        for i in range(2**j):
            bin_ = binaries(i, j)
            printOne_D(bin_)
            print("-"*20)
        print('*'*30)