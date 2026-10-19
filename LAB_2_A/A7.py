x1 = int(input("Введите координату х для 1 точки\n"))
y1 = int(input("Введите координату y для 1 точки\n"))
x2 = int(input("Введите координату х для 2 точки\n"))
y2 = int(input("Введите координату y для 2 точки\n"))
xy1 = x1 + y1
xy2 = x2 + y2

if xy1 % 2 == 0 :
    c1 = "White" 
else :
    c1 = "Black"

if xy2 % 2 == 0 :
    c2 = "White" 
else :
    c2 = "Black"

if c1 == c2 :
    print("YES")
    print(c1)
else:
    print("NO")