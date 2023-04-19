from tkinter import *
from tkinter import messagebox

def item_calc():
    item_width = int(item_width_tf.get())
    item_length = int(item_length_tf.get())
    sheet_width = int(sheet_width_tf.get())
    sheet_length = int(sheet_length_tf.get())
    borders = int(borders_tf.get())
    distance = int(distance_tf.get())

    tall_album = int((sheet_width-(borders*2))/(item_width+distance))
    wide_album = int((sheet_length-(borders*2))/(item_length+distance))
    tall_vert = int((sheet_length-(borders*2))/(item_width+distance))
    wide_vert = int((sheet_width-(borders*2))/(item_length+distance))

    messagebox.showinfo('Результат',
                        "В альбомной ориентации количество элементов \nпо вертикали: %s" \
                        " \nпо горизонтали: %s," \
                        " \nобщее количество элементов: %s.\n"\
                        " \nВ книжной ориентации количество элементов \nпо вертикали: %s," \
                        " \nпо горизонтали: %s," \
                        " \nобщее количество элементов: %s."\
                        % (tall_album, wide_album, tall_album*wide_album, tall_vert, wide_vert, tall_vert*wide_vert))

window = Tk()
window.title('Калькулятор изделий на листе')
window.geometry('400x200')

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

item_width_lb = Label(frame, text='Введите ширину изделия, мм')
item_length_lb = Label(frame, text='Введите длину изделия, мм:')
sheet_width_lb = Label(frame, text='Введите ширину листа, мм:')
sheet_length_lb = Label(frame, text='Введите длину листа, мм:')
borders_lb = Label(frame, text='Введите отступы от края листа, мм:')
distance_lb = Label(frame, text='Введите расстояние между изделиями, мм:')

item_width_lb.grid(row=1, column=1)
item_length_lb.grid(row=2, column=1)
sheet_width_lb.grid(row=3, column=1)
sheet_length_lb.grid(row=4, column=1)
borders_lb.grid(row=5, column=1)
distance_lb.grid(row=6, column=1)

item_width_tf = Entry(frame)
item_length_tf = Entry(frame)
sheet_width_tf = Entry(frame)
sheet_length_tf = Entry(frame)
borders_tf = Entry(frame)
distance_tf = Entry(frame)

item_width_tf.grid(row=1, column=2)
item_length_tf.grid(row=2, column=2)
sheet_width_tf.grid(row=3, column=2)
sheet_length_tf.grid(row=4, column=2)
borders_tf.grid(row=5, column=2)
distance_tf.grid(row=6, column=2)

calc_btn = Button(frame, text='Ввод', command=item_calc)
calc_btn.grid(row=7, column=2)

window.mainloop()