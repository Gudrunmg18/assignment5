n = int(input("Enter the length of the sequence: ")) # Do not change this line

#n = length(rod)
number1 = 1
number2 = 2
number3 = 3
print(number1)
print(number2)
print(number3)

for i in range(n - 3):
    summa = number1 + number2 + number3
    number1 = number2
    number2 = number3
    number3 = summa
    print(summa)

