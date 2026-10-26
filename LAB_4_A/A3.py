info = list(input("Ввод информации о доставке пакетов данных\n"))
result_1 = set(info).issubset({"0", "1"})

if len(info) < 5 :
    print("Слишком короткий пакет данных\n")
elif result_1 == False :
    print("Недопустимо использование инных символов\n")

print(f"Общее количество пакетов: {len(info)}")

ones_count = info.count('1')
zeros_count = info.count('0')

from itertools import groupby
out_paks_max = max(len(list(group)) for key, group in groupby(info))

procent_loss =  round((zeros_count / len(info)) * 100, 1)
print(f"Количество потеряных пакетов: {zeros_count}")
print(f"Длинна самой длинной последовательности потеряных пакетов: {out_paks_max} ")
print(f"Процент потерь: {procent_loss}%")

if procent_loss <= 1 :
    print("Качество связи: Отличное качество")
elif 1 < procent_loss <= 5 :
    print("Качество связи: Хорошее качество")
elif 5 < procent_loss <= 10 :
    print("Качество связи: Удовлетворительное качество")
elif 10 < procent_loss <= 20 :
    print("Качество связи: Плохое качество")
elif procent_loss > 20 :
    print("Качество связи:  Критическое состояние сети")