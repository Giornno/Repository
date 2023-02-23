price=0
ticket=int(input("Сколько билетов хотите купить: "))
for i in range(ticket):
    i+=1
    age=int(input(f'введите возраст посетителя по {i} билету'))
    if age<18:
        print('проход бесплатный')
    elif 18 <= age < 25:
        price+=990
        print("цена билета: 990 рублей")
    elif age>= 25:
        price+= 1390
        print("цена билета: 1390 рублей")
if ticket > 3:
    price_discount = price - (price * 0.1)
    print(f"сумма к оплате с учётом скидка: {price_discount} рублей")
else:
    print(f"итого к оплате {price} рублей")