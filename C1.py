a, b, c = 3, 1, -1
def main():
    global a, b
    while a > c:
        if a == 0:
            print b
        else:
            b = b + a
        a = a - 1
    print a
    print b
    print c
main()
