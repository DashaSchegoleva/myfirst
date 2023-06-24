def polindrom(c):
    if c==c[::-1]:
        print(True)
    else:
        print(False)
    
c = input()
polindrom(c)
