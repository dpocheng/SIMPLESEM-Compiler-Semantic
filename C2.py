n = 0; m = 0;

def gcd():
    global n, m
    while m != n:
        if(n > m):
            n = n - m
        else:
            m = m - n

def main():
    #get(n, m)
    global n, m
    n = 10
    m = 35
    gcd()
    print n

main()
