k1 = int(input("Введите показания счетчика для предыдущего месяца\n"))
k2 = int(input("Введите показания счетчика сейчас\n"))
if k2 < k1 :
    month_cube_consum = k2 + 10000 - k1
else:
    month_cube_consum = k2 - k1

if month_cube_consum <= 300 :
    price = 21
elif 300 < month_cube_consum <= 600 :
    price = 21 + ((month_cube_consum - 300) * 0.06)
elif 600 < month_cube_consum <= 800 :
    price = 21 ((month_cube_consum - 300) * 0.04)
elif month_cube_consum > 800 :
    price = month_cube_consum * 0.025
 
mid_price = price / month_cube_consum
price = round(price, 2)
mid_price = round(mid_price, 2) 
print("Предыдущее значение", "  Текущее   ", "Использовано      " "К оплате" "      Ср.цена m^3" "\n")
print(f"   {k1}                  {k2}          {month_cube_consum}          {price}              {mid_price}")