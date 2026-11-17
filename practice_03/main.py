# Практика 3. Вариант 22: генераторное выражение и декоратор.


def announce(func):
    def wrapper():
        print("Внимание")
        return func()

    return wrapper


@announce
def hello():
    print("Привет!")


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6]
    g = (x for x in numbers if x > 2)
    print(list(g))
    hello()
