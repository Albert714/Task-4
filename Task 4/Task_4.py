a = int(input())
bb = (a%100//10)**(a%10) # предпоследнее введенное число возводим в степень последнего введенного числа
cc = bb * (a%1000//100) # умножаем полученное число на 3е введенное число
dd = (a%100000//10000)-(a%10000//1000) # находим разность между первым и вторым числом
ee = cc/dd
print(ee)
