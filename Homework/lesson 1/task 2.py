print("Введите x: ")
x = int(input())
print("Введите y: ")
y = int(input())
print("x=" + str(x) + " y=" + str(y))


# x = -100
# y = 20

def task1(x, y):
    print("Задание1. x=" + str(x) + " y=" + str(y))
    if x <= -2 and y >= 1:
        print("Точка внутри области.")
    else:
        print("Точка не попадает в область.")
    print()


def task2(x, y):
    print("Задание2. x=" + str(x) + " y=" + str(y))
    if -2 <= y <= 1.5:
        print("Точка внутри области.")
    else:
        print("Точка не попадает в область.")
    print()


def task3(x, y):
    print("Задание3. x=" + str(x) + " y=" + str(y))
    if 1 <= x <= 2 and y <= 4:
        print("Точка внутри области.")
    else:
        print("Точка не попадает в область.")
    print()


def task4(x, y):
    print("Задание4. x=" + str(x) + " y=" + str(y))
    if x >= 1 and 2 <= y <= 4:
        print("Точка внутри области.")
    else:
        print("Точка не попадает в область.")
    print()


def task5(x, y):
    print("Задание5. x=" + str(x) + " y=" + str(y))
    if (x >= 1 and y <= -1) or (x >= 2 and y >= 0):
        print("Точка внутри области.")
    else:
        print("Точка не попадает в область.")
    print()


def task6(x, y):
    print("Задание6. x=" + str(x) + " y=" + str(y))
    if (x >= 2 and y >= 1) or (x >= 2 and y <= -1.5):
        print("Точка внутри области.")
    else:
        print("Точка не попадает в область.")
    print()


def task7(x, y):
    print("Задание7. x=" + str(x) + " y=" + str(y))
    if (1 <= x <= 3) and (-2 <= y <= -1):
        print("Точка внутри области.")
    else:
        print("Точка не попадает в область.")
    print()


def task8(x, y):
    print("Задание8. x=" + str(x) + " y=" + str(y))
    if (1.5 >= y >= 0.5) and x >= 2:
        print("Точка внутри области.")
    else:
        print("Точка не попадает в область.")
    print()


if __name__ == "__main__":
    task1(x, y)
    task2(x, y)
    task3(x, y)
    task4(x, y)
    task5(x, y)
    task6(x, y)
    task7(x, y)
    task8(x, y)
