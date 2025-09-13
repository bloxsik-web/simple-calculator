print(" ")
print(" ᴄᴀʟᴄᴜʟᴀᴛᴏʀ")
print("ʙʏ ʙʟᴏxsɪᴋ-ᴡᴇʙ")
print(" ")

num1 = input("Введите первое значение: ")
num2 = input("Введите второе значение: ")
wtf = input("Что хотите сделать? (+, -, *, /): ")

if wtf == "+":
 print ("Результат:",int(num1) + int(num2))
elif  wtf == "-":
 print ("Результат:",int(num1) - int(num2))
elif  wtf == "*":
 print ("Результат:",int(num1) * int(num2))
elif  wtf == "/":
 print ("Результат:",int(num1) // int(num2))
else:
 print ("Не известная операция, попробуйте + для прибавления, - для убавления, * для умножения, / для умножения для деления.")
