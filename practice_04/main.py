# Практика 4. Вариант 22: функции в Python.

# 1. Область видимости.
x = 32


def show():
    x = 22
    print(x)


show()
print(x)

# Вывод: сначала 22, затем 32.
# В show() используется локальное x = 22, снаружи — внешнее x = 32.
# Присваивание внутри функции не меняет внешнюю переменную.


# 2. Позиционные аргументы.
def total(*args):
    return sum(args)


print(total(22, 23, 24))


# 3. Именованные аргументы.
def person(**kwargs):
    name = kwargs.get("name", "Гость")
    age = kwargs.get("age", 0)
    return name, age


print(person(name="Соня", age=18))


# 4. Функция как параметр.
def increase(x):
    return x + 2


def apply(func, value):
    return func(value)


print(apply(increase, 3))


# 5. Рекурсивный отсчёт.
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)


countdown(3)
