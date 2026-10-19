x1 = float(input("введите х1\n"))
y1 = float(input("введите y1\n"))
x2 = float(input("введите х2\n"))
y2 = float(input("введите y2\n"))
if x1 == 0 or x2 == 0 or y1 == 0 or y2 == 0 :
    print("точка находится на границе четвертей")
else:
    if y1 > 0 :
        if x1 > 0 :
            d1 = 1
        else:
            d1 = 2
    else:
        if x1 > 0 :
            d1 = 4
        else:
            d1 = 3

    if y2 > 0 :
        if x2 > 0 :
            d2 = 1
        else:
            d2 = 2
    else:
        if x2 > 0 :
            d2 = 4
        else:
            d2 = 3

    if d1 == d2 :
        print("YES")
        if d1 == 1 :
            print(1)
        elif d1 == 2 :
            print(2)
        elif d1 == 3 :
            print(4)
        else:
            print(4)
    else:
        print("NO")