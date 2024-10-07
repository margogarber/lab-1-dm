# LAB_1
# Task 1
def task_1():
    a = (input("Enter a: "))
    if a.isnumeric():
        a = float(a)
    else:
        print('Можна вводити тільки числа')
        task_1()
    b = (input("Enter b: "))
    if b.isnumeric():
        b = float(b)
    else:
        print('Можна вводити тільки числа')
    print(a * b)
    print(2 * (a + b))


# Task 2
def task_2():
    a = (input("Enter a: "))
    if a.isnumeric():
        a = float(a)
    else:
        print("only numbers")
        task_2()
    b = (input("Enter b: "))
    if b.isnumeric():
        b = float(b)
    else:
        print("only numbers")
        task_2()
    gem_mid = (a * b) ** 0.5
    print("Середнє геометричне: ", gem_mid)


# Task 3
def task_3():
    x1 = (input("Enter x1: "))
    if x1.isnumeric():
        x1 = float(x1)
    else:
        print("only numbers")
        task_3()
    x2 = (input("Enter x2: "))
    if x2.isnumeric():
        x2 = float(x2)
    else:
        print("only numbers")
        task_3()
    y1 = (input("Enter y1: "))
    if y1.isnumeric():
        y1 = float(y1)
    else:
        print("only numbers")
        task_3()
    y2 = (input("Enter y2: "))
    if y2.isnumeric():
        y2 = float(y2)
    else:
        print("only numbers")
        task_3()
    lenght = abs(x2 - x1)
    width = abs(y2 - y1)
    area = lenght * width
    perimeter = 2 * (lenght + width)
    print("Area is", area)
    print("Perimeter is", perimeter)


# Task 4
def task_4():
    a = input("Enter a: ")
    try:
        a = float(a)
        if a % 2 == 0:
            print(f"{a} є парним.")
        else:
            print(f"{a} не є парним.")
    except ValueError:
        print("Можна вводити тільки числа.")
        task_4()


# Task 5
def task_5():
    a = input("Enter a: ")
    b = input("Enter b: ")
    c = input("Enter c: ")
    
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        
        if a < b < c:
            print("true")
        else:
            print("false")
        
        if a > 0 or b > 0 or c > 0:
            print("хоча б одне з чисел додатне")
        else:
            print("жодне з чисел не є додатним")

        if (a > 0) + (b > 0) + (c > 0) == 1:
            print("рівно одне з чисел додатне")
        else:
            print("рівно одне з чисел додатне false")
    except ValueError:
        print("Можна вводити тільки числа.")
        task_5()

        
# Task 6
def task_6():
    x = input("Enter x: ")
    y = input("Enter y: ")
    
    if x.isnumeric() and y.isnumeric():
        x = float(x)
        y = float(y)
        if (x + y) % 2 != 0:
            print(f"Поле ({x}, {y}) є білим.")
        else:
            print(f"Поле ({x}, {y}) є чорним.")
    else:
        print("Можна вводити тільки числа.")
        task_6()



# Task 7
def task_7():
    x1 = input("Enter x1 (1-8): ")
    x2 = input("Enter x2 (1-8): ")
    y1 = input("Enter y1 (1-8): ")
    y2 = input("Enter y2 (1-8): ")
    
    if x1.isnumeric() and x2.isnumeric() and y1.isnumeric() and y2.isnumeric():
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        
        # Перевірка, чи всі введені числа знаходяться в межах від 1 до 8
        if all(1 <= num <= 8 for num in [x1, x2, y1, y2]):
            if x1 == x2 or y1 == y2 or abs(x2 - x1) == abs(y2 - y1):
                print(f"Ферзь може перейти з поля ({x1}, {y1}) на поле ({x2}, {y2}) за один хід.")
            else:
                print(f"Ферзь не може перейти з поля ({x1}, {y1}) на поле ({x2}, {y2}) за один хід.")
        else:
            print("Можна вводити тільки числа в діапазоні від 1 до 8.")
            task_7()
    else:
        print("Можна вводити тільки числа від 1 до 8.")
        task_7()


# Task 8
def task_8():
    a = input("Enter a: ")
    b = input("Enter b: ")
    
    if a.isnumeric() and b.isnumeric():
        a = int(a)
        b = int(b)
        numb = list(range(a, b + 1))
        print(f"Числа від {a} до {b}: {numb}")
        print(f"Кількість чисел: {len(numb)}")
    else:
        print("Можна вводити тільки числа.")
        task_8()


# Task 9
def task_9():
    N = input("Enter N: ")
    
    if  N.isnumeric():  
        N_reversed = N[::-1]  
        print(f"Число {N} обернене: {N_reversed}")
    else:
        print("Можна вводити тільки числа.")
        task_9()


# Task 10
def task_10():
    try:
        b = list(map(int, input("Введіть 5 чисел через пробіл: ").split()))
        if len(b) != 5:
            print("Введіть рівно 5 чисел!")
        else:
            a = sum(b) / len(b)
            for i in range(len(b)):
                if b[i] > a:
                    b[i] -= 18
            print(f"Масив: {b}")
            print(f"Середнє значення: {a}")
    except ValueError:
        print("Можна вводити тільки числа!")


# Task 11
def task_11():
    N = int(input("enter N:"))
    if N > 1:
        num = True
        for i in range(2, int(N**0.5)+1):
            if N % i == 0:
                num = False
                break 
    if num:
            print("true")
    else:
            print("false")


# Task 12
def task_12():
    import math 
    x = 6
    y = 6.63
    z = -2
    a = (math.sqrt(x ** 3 + y ** 2) + z )
    print("a is", a)


# Task 13
def task_13():
    first_name = str(input("Введіть своє ім'я: "))
    last_name = str(input("Введіть своє прізвище: "))
    phone = str(input("Введіть свій номер телефону(необов'язково): "))
    if not first_name and not last_name:
        print("Не залишайте жодні поля порожніми")
    else: 
        print("Спасибі")


# Task 14
def task_14():
    for counter in range(5):
        numb = input("Введіть число: ")
        if numb.isnumeric():
            numb = int(numb)
            if numb == 5:
                print("Правильно, ви умнічка!!!")
                break
            else:
                print(f"Спроба №{counter + 1}: Ви ввели {numb}, спробуйте ще раз.")
        else:
            print("Можна вводити тільки числа.")
    else:
        print("Нажаль не вірно :( спробуйте ще.")


# Task 15
def task_15():
    for numb in range (13, 100, 13): 
        print(numb)


# Task 16
def task_16():
    string_1 = "Привіт Світ!"
    print("Перший рядок:", string_1)
    try:
        string_1[0] = "b"
    except TypeError as e:
        print("Помилка:", e)  
    string_2 = "Допобаченя Світ!" 
    print("Другий рядок:", string_2)
    string_1_2 = string_1 + string_2 
    print("Об'єднаний рядок:", string_1_2)
    mul_string = string_1 * 10
    print("Перший рядок 10 разів:", mul_string)
    string_mod = string_1_2[:6] + "!" + string_1_2
    print("Змінений рядок:", string_mod)
    string_1_mod = string_1[:12] + ":)" 


m = int(input('Choose task: '))
arr = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13, task_14, task_15, task_16]
try:
    arr[m-1]() 
except IndexError:
    print('Всього 16 завдань')