import random
import json
import os

QUOTES_FILE = "quotes.json"

# Загрузка цитат из json файла
def load_quotes():
    if os.path.exists(QUOTES_FILE):
        with open(QUOTES_FILE, "r", encoding='utf-8') as file:
            quotes = json.load(file)
    else:
        quotes = []
    return quotes

# Сохранение цитат в json файл
def save_quotes(quotes):
    with open(QUOTES_FILE, "w", encoding='utf-8') as file:
        json.dump(quotes, file, indent=4)

# Получение случайной цитаты
def get_random_quote(quotes):
    return random.choice(quotes)

# Добавление новой цитаты
def add_new_quote(quotes):
    quote = input("Введите новую цитату: ")
    author = input("Введите автора цитаты: ")

    new_quote = {
        "quote": quote,
        "author": author
    }

    quotes.append(new_quote)
    save_quotes(quotes)

    print("Новая цитата добавлена!")

# Основной цикл чат-бота
def main():
    quotes = load_quotes()
    print("Привет! Я чат-бот с цитатами известных людей.")
    print("Напиши 'цитата', чтобы получить случайную цитату.")
    print("Напиши 'добавить', чтобы добавить новую цитату.")
    print("Напиши 'выход', чтобы выйти из программы.")

    while True:
        user_input = input("> ").lower()

        if user_input == "цитата":
            if not quotes:
                print("Цитаты отсутствуют.")
            else:
                quote = get_random_quote(quotes)
                print(f"Цитата: {quote['quote']}")
                print(f"Автор: {quote['author']}")
        elif user_input == "добавить":
            add_new_quote(quotes)
        elif user_input == "выход":
            print("До свидания!")
            break
        else:
            print("Извини, я не понял команду. Попробуй еще раз.")

if __name__ == "__main__":
    main()