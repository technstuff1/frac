def cont(a):
    a = str(a)
    x = -1
    y = 0
    for i in a:
        x = x + 1
        if i == "_":
            z = ''
            for g in range(len(str(a[x:-1]))):
                z = z + "9"
            z = int(z)
            a = float(float(a[0:x]) + float(a[x+1:len(a)])/z)
            y = 1
    if y == 0:
        a = float(a)
    n = 1
    d = 1
    b = 1
    while a != b:
        b = n/d
        if a > b:
            n = n + 1
        elif a < b:
            d = d + 1
        else:
            pass
    return(n/d)