import random
import time

N = int(input("Ведите  количество примеров:\n"))
start_all_time = time.perf_counter()
T = 0
for i in range(1, N + 1):

    print(f"Вопрос {i}/{N}")

    x = random.randint(2, 9)
    y = random.randint(2, 9)
    z = x * y

    start_t = time.perf_counter()

    while True:
        try:
            k = float(input(f"{x} x {y} = "))
            if k % 1 != 0 :
                print("Пожалуйста, введите целое число!")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")

    end_t = time.perf_counter()
    t = round(end_t - start_t, 1)

    if k == z:
        print(f"Верно!(Время: {t} сек)")
        T += 1
    else:
        print(f"Неверно! Правильно: {z} (Время: {t} сек)")

end_all_time = time.perf_counter()
all_time = round(end_all_time - start_all_time, 1)

print("=" * 30)
print("СТАТИСТИКА:")
print("=" * 30)
print(f"Общеее время: {all_time} секунд")
print(f"Среднее время на вопрос: {round(all_time / N, 1)} секунд")
print(f"Правильных ответов: {T}/{N}")
print(f"Процент правильных: {round((T / N) * 100, 1)}%")