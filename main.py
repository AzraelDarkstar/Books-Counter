# Импортируем библиотеки для работы с файлами
import json
from os.path import exists

# Импортируем функции из библиотеки tkinter 
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import askyesno

# Функция для обновления данных
def update():
    save(books_list)            # Cохраняем итоговый список в файл
    List.delete(0, END)         
    for book in books_list:     # Перезаписываем наш
        List.insert(0, book)    # ListBox

# Функция для чтения  данных из файлa
def load():
    if exists('list.json'):                      # Проверка на существование файла
        with open('list.json', 'r') as file:
            books = json.load(file)
    else: books = []                              # Иначе создаем пустой список
    return books    

# Функция для записи данных в файл
def save(books):
    with open('list.json', 'w') as file:
        json.dump(books, file)


# Далее представлены функции для кнопок

        
def add():
    new_book = name.get().title().strip()              # Получаем данные из Entry, переводим первые буквы в верхний регистр, удаляем лишние пробелы
    if new_book not in books_list and new_book != '':  # Проверка на дупликаты
        books_list.append(new_book)
    name.delete(0, END)             # Очищаем Entry
    update()
    
def delete():
    num = List.curselection()               # Получаем индекс выбраного элемента
    books_list.remove(List.get(num))        # Удаляем выбраный элемент из списка
    update()
    
def clear():
    res = askyesno(title='Подтверждение', message='Вы уверены что хотите удалить все данные?')  # Вызываем окно подтверждения
    if res:
        books_list.clear()          # Очищаем список
        update() 
        
def font_changed(font):
    List["font"] = font

def select_font():
    root.tk.call("tk", "fontchooser", "configure", "-font", List["font"], "-command", root.register(font_changed))
    root.tk.call("tk", "fontchooser", "show")
  

# Настройки окна
root = Tk()
root.title('Book Counter')
root.geometry("350x320+500+300")
root.resizable('False', 'False')
root.iconbitmap(default="icon.ico")

# Сохраняем список из файла в переменную books_list, для удобной работы с ним
books_list = load()


# Задаем виджеты и добавляем их в окно
labe = ttk.Label(text="Введите название книги:")
labe.grid(row=0,column=0)

name = ttk.Entry()
name.grid(column=0, row=1, padx=6, pady=6, sticky=EW)

addBtn = ttk.Button(text='Добавить', command=add)
addBtn.grid(column=1, row=1, padx=6, pady=6)

List = Listbox(selectbackground='RED')
List.grid(row=2, column=0, columnspan=4, sticky=EW, padx=6, pady=6)

delBtn = ttk.Button(text='Удалить', command=delete)
delBtn.grid(row=3, column=2, columnspan=2, sticky=EW, padx=6, pady=6)

clearBtn = ttk.Button(text='Очистить Все', command=clear)
clearBtn.grid(row=3, column=0, sticky=EW, padx=6)

settings = ttk.Button(text="Выбрать шрифт", command=select_font)
settings.grid(row=3, column=1)


update()
root.mainloop() # Необходимо для функционирования