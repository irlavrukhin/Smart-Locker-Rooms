from tkinter import *
from tkinter import ttk
# import sqlite3
import read_text


# функция для вывода информации после нажатия на кнопку
def clicked():
    lbl.configure(text='Заказ уже в пути')
    lbl2.configure(text='Заказ уже в пути')


# функция для очистки дополнительного образа
def clear_add_look():
    epc_range = read_text.read_range_of_epc()
    len_of_epc_range = len(epc_range)
    print(len_of_epc_range)
    if len_of_epc_range == 0:
        im5.configure(file='images/0.gif')
        label_5.configure(image=im5)

        im6.configure(file='images/0.gif')
        label_6.configure(image=im6)

        im7.configure(file='images/0.gif')
        label_7.configure(image=im7)


# функция для кнопки обновления образа
def refresh_of_look():
    im5.configure(file='images/look_1/panama.gif')
    label_5.configure(image=im5)

    im6.configure(file='images/look_1/glass.gif')
    label_6.configure(image=im6)

    im7.configure(file='images/look_1/shlepki.gif')
    label_7.configure(image=im7)


# функция для обновления состояния окна с товаром на первой вкладке
def refresh():
    # обработка ошибки - если файл пустой, то EPC присваивается 0
    try:
        # вызов модуля для чтения файла
        EPC = read_text.read_epc_set()
        EPC = list(EPC)
        EPC.sort()
    except UnboundLocalError:
        EPC = [0]
    # печать номерка в консоль
    if EPC == []:
        EPC.append('0')
        EPC = EPC * 10
    print(len(EPC))
    print(EPC)
    len_of_epc_list = len(EPC)
    print('--------------------------------------------------')
    if (EPC[0].split())[0] == '3039ECBC018726012A05F537':
        # im0.configure(file='images/5.gif')
        # label_0.configure(image=im0)

        im1.configure(file='images/look_1/shirt.gif')
        label_1.configure(image=im1)

        im2.configure(file='images/look_1/cap.gif')
        label_2.configure(image=im2)

        im3.configure(file='images/look_1/bridji.gif')
        label_3.configure(image=im3)

        im4.configure(file='images/look_1/boti.gif')
        label_4.configure(image=im4)

        # обновление через каждую секунду
        label_1.after(1000, refresh)
    elif (EPC[0].split())[0] == '00B07A13F41269080BFFE3D5':
        # im0.configure(file='images/5.gif')
        # label_0.configure(image=im0)

        im1.configure(file='images/look_2/west_side.gif')
        label_1.configure(image=im1)

        im2.configure(file='images/look_2/cross.gif')
        label_2.configure(image=im2)

        im3.configure(file='images/look_2/barbour.gif')
        label_3.configure(image=im3)

        im4.configure(file='images/look_2/dolce.gif')
        label_4.configure(image=im4)

        # обновление через каждую секунду
        label_1.after(1000, refresh)
    elif (EPC[0].split())[0] == '3034F7A3245CA29040000064':
        # im0.configure(file='images/5.gif')
        # label_0.configure(image=im0)

        im1.configure(file='images/look_3/footboul.gif')
        label_1.configure(image=im1)

        im2.configure(file='images/look_3/short.gif')
        label_2.configure(image=im2)

        im3.configure(file='images/look_3/getri.gif')
        label_3.configure(image=im3)

        im4.configure(file='images/look_3/buts.gif')
        label_4.configure(image=im4)

        # обновление через каждую секунду
        label_1.after(1000, refresh)
    elif (EPC[0].split())[0] == '3034F7D5745FAFC0367002A0':
        # im0.configure(file='images/5.gif')
        # label_0.configure(image=im0)

        im1.configure(file='images/look_4/rubakha.gif')
        label_1.configure(image=im1)

        im2.configure(file='images/look_4/babochka.gif')
        label_2.configure(image=im2)

        im3.configure(file='images/look_4/pidzak.gif')
        label_3.configure(image=im3)

        im4.configure(file='images/look_4/bruki.gif')
        label_4.configure(image=im4)

        # обновление через каждую секунду
        label_1.after(1000, refresh)
    else:
        # im0.configure(file='images/0.gif')
        # label_0.configure(image=im0)
        # вызов функции очистки
        clear_add_look()
        im1.configure(file='images/0.gif')
        label_1.configure(image=im1)

        im2.configure(file='images/0.gif')
        label_2.configure(image=im2)

        im3.configure(file='images/0.gif')
        label_3.configure(image=im3)

        im4.configure(file='images/0.gif')
        label_4.configure(image=im4)

        label_1.after(1000, refresh)


# создание окна
window = Tk()
window.title("Добро пожаловать в Умную примерочную")
# задание размеров окна
window.geometry('800x600')

# создание вкладок
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Все, что вы принесли')
tab_control.add(tab2, text='Дополнение образа')
# tab_control.add(tab3, text='Вы можете заказать ко второй вещи')
tab_control.pack(expand=1, fill='both')

# создание надписей на всех вкладках
lbl = Label(tab1, text="Добро пожаловать", font=("Arial", 20))
lbl.grid(column=0, row=0)
lbl2 = Label(tab2, text="Добро пожаловать", font=("Arial", 20))
lbl2.grid(column=0, row=0)
lbl3 = Label(tab3, text="Добро пожаловать", font=("Arial", 20))
lbl3.grid(column=0, row=0)

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

# кнопка для обновления образа
btn8 = Button(tab2, text="Обновить образ", bg='black', fg='white', command=refresh_of_look, font=("Arial", 15))
btn8.grid(column=6, row=0)

# лейбл для первой вкладки, где происходит считывание вещи
im1 = PhotoImage(file='images/0.gif')
label_1 = Label(tab1, image=im1)
label_1.grid(column=2, row=3)

# лейблы для второй вкладки, где происходит подбор образа
im2 = PhotoImage(file='images/0.gif')
label_2 = Label(tab2, image=im2)
label_2.grid(column=3, row=2)

im3 = PhotoImage(file='images/0.gif')
label_3 = Label(tab2, image=im3)
label_3.grid(column=3, row=3)

im4 = PhotoImage(file='images/0.gif')
label_4 = Label(tab2, image=im4)
label_4.grid(column=3, row=4)

# лейблы для третьей вкладки, где происходит подбор образа
im5 = PhotoImage(file='images/0.gif')
label_5 = Label(tab2, image=im5)
label_5.grid(column=5, row=2)

im6 = PhotoImage(file='images/0.gif')
label_6 = Label(tab2, image=im6)
label_6.grid(column=5, row=3)

im7 = PhotoImage(file='images/0.gif')
label_7 = Label(tab2, image=im7)
label_7.grid(column=5, row=4)

# создание базы данных
# conn = sqlite3.connect("mydatabase.db")
# cursor = conn.cursor()
# Создание таблицы, если она не существует
# cursor.execute("""CREATE TABLE if not exists EPC_Numbers
#                   (EPC text, Image text)
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
