#  Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд 
# и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no


ticket_number = int(input("Введите номер билета: "))
if len(str(ticket_number)) != 6:
    print("no")
else:
    first_part = ticket_number // 1000 
    second_part = ticket_number % 1000 
    first_sum = 0
    second_sum = 0
    while first_part > 0: 
        digit = first_part % 10 
        first_sum += digit 
        first_part //= 10 
    while second_part > 0: 
        digit = second_part % 10 
        second_sum += digit 
        second_part //= 10 
    if first_sum == second_sum:   
        print("yes")              
    else:                        
        print("no")