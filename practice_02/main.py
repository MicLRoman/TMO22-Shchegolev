# Практика 2. Вариант 22: снимков в альбоме.


def photos_per_album(photos, albums):
    if albums == 0:
        return "На ноль делить нельзя"
    return photos / albums


if __name__ == "__main__":
    assert photos_per_album(120, 6) == 20.0
    assert photos_per_album(120, 0) == "На ноль делить нельзя"
    assert photos_per_album(15, 2) == 7.5

    words = ["фон", "камера", "фотография"]
    sorted_words = sorted(words, key=lambda word: len(word))
    print(sorted_words)
