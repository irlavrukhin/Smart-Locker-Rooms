from tkinter import *
from tkinter import ttk
import sqlite3
import read_text

order = 0
print(order)


# функция для вывода информации после нажатия на кнопку
def clicked():
    lbl.configure(text='Заказ уже в пути')
    lbl2.configure(text='Заказ уже в пути')
    order = 1
    print(order)


# функция для обновления состояния окна с товаром на первой вкладке
def refresh():
    # обработка ошибки - если файл пустой, то EPC присваивается 0
    try:
        # вызов модуля для чтения файла
        EPC = read_text.read_epc()
    except UnboundLocalError:
        EPC = [0]
    # печать номерка в консоль
    # print(EPC[0])
    if EPC[0] == '3034F7A32414EE8040A00462':
        im1.configure(file='5.gif')
        l1.configure(image=im1)

        im2.configure(file='6.gif')
        l2.configure(image=im2)

        im3.configure(file='7.gif')
        l3.configure(image=im3)

        im4.configure(file='8.gif')
        l4.configure(image=im4)

        # обновление через каждую секунду
        l1.after(1000, refresh)
    else:
        im1.configure(file='0.gif')
        l1.configure(image=im1)

        im2.configure(file='0.gif')
        l2.configure(image=im2)

        im3.configure(file='0.gif')
        l3.configure(image=im3)

        im4.configure(file='0.gif')
        l4.configure(image=im4)

        l1.after(1000, refresh)


# создание окна
window = Tk()
window.title("Добро пожаловать в Умную примерочную")
# задание размеров окна
window.geometry('800x600')

# создание вкладок
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Все, что вы принесли')
tab_control.add(tab2, text='Все, что вы можете заказать')
tab_control.pack(expand=1, fill='both')

# создание надписей на обеих вкладках
lbl = Label(tab2, text="Добро пожаловать", font=("Arial", 20))
lbl.grid(column=0, row=0)
lbl2 = Label(tab1, text="Добро пожаловать", font=("Arial", 20))
lbl2.grid(column=0, row=0)

# создание кнопки на первой вкладке
# btn1 = Button(tab1, text="Обновить", bg='black', fg='white', command=refresh, font=("Arial", 15))
# btn1.grid(column=6, row=0)

# создание кнопок во второй вкладке
btn2 = Button(tab2, text="Принести", bg='black', fg='white', command=clicked, font=("Arial", 15))
btn2.grid(column=4, row=2)
btn3 = Button(tab2, text="Принести", bg='black', fg='white', command=clicked, font=("Arial", 15))
btn3.grid(column=4, row=3)
btn4 = Button(tab2, text="Принести", bg='black', fg='white', command=clicked, font=("Arial", 15))
btn4.grid(column=4, row=4)

# создание лейбла внутри которого помещена картинка
im1 = PhotoImage(file='0.gif')
l1 = Label(tab1, image=im1)
l1.grid(column=2, row=3)

im2 = PhotoImage(file='0.gif')
l2 = Label(tab2, image=im2)
l2.grid(column=3, row=2)

im3 = PhotoImage(file='0.gif')
l3 = Label(tab2, image=im3)
l3.grid(column=3, row=3)

im4 = PhotoImage(file='0.gif')
l4 = Label(tab2, image=im4)
l4.grid(column=3, row=4)

# создание базы данных
# conn = sqlite3.connect("mydatabase.db")
# cursor = conn.cursor()
# Создание таблицы, если она не существует
# cursor.execute("""CREATE TABLE if not exists EPC_Numbers
#                   (EPC text)
#                """)

# обращаемся к бд в столбец EPC; мы хотим выбрать все записи, подходящие под переданное имя исполнителя
# sql = "SELECT * FROM EPC_Numbers WHERE EPC=?"
# cursor.execute(sql, [(EPC[0])])
# number_of_epc = cursor.fetchall()
# print(number_of_epc[0][0])
# print(type(number_of_epc[0][0]))

refresh()
# бесконечный вызов окна
window.mainloop()
