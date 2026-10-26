n = int(input("Введите высоту \n"))
m = int(input("Введите длинну \n"))

print(f"ПРЯМОУГОЛЬНИК {n}x{m}:")
for i in range(n):
    print(m * "#")

print("ПРАВЫЙ ТРЕУГОЛЬНИК:")
for j in range(1, n):
    print(j * "#")

print(f"РАМКА {n}x{m}:")
print(m * "#")

for k in range(n - 2):
        print("#" + (m - 2) * " " + "#")

print(m * "#")