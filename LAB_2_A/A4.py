A = int(input("Введите число А\n"))
B = int(input("Введите число В\n"))
if (1>A or A>1000) or (1>B or B>1000):
    print("Введенное число меньше 1 или 1000\n")
elif A == B:
    print("Оба числа равны")
elif A > B:
    print(A)
else:
    print(B)