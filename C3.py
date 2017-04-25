globalN = 0
def c3():
    global globalN
    n = globalN
    globalN = globalN - 1
    if (n == 1):
        return 1
    else:
        return 2*c3() + 1

def main():
    global globalN
    globalN = 3
    print c3()

main()
