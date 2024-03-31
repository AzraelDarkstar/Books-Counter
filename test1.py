import json
from os.path import exists

def load():
    if exists('list.json'):
        with open('list.json', 'r') as file:
            books = json.load(file)
    else: books = []
    return books

def save(books):
    with open('list.json', 'w') as file:
        json.dump(books, file)

books_list = load()

new_book = input('Введите название новой книги: ')

books_list.append(new_book)

save(books_list)

for book in books_list:
    print(f"{book}")
