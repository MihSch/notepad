from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

def notepad_exit():
    answer = messagebox.askokcancel('Выход', 'Вы точно хотите выйти?')
    if answer:
        root.destroy()


def open_file():
    file_path = filedialog.askopenfilename(title='Выбор файла', filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    if file_path:
        text_fild.delete('1.0', END)
        text_fild.insert('1.0', open(file_path, encoding='utf-8').read())


def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    f = open(file_path, 'w', encoding='utf-8')
    text = text_fild.get('1.0', END)
    f.write(text)
    f.close()

def info_prog():
    answer = messagebox.showinfo('info','''
    Дата создания: 27.10.2024
    Создатель: MihSch
    ''')
    return answer

root = Tk()
root.title('Блокнот')
root.geometry('600x600')

main_menu = Menu(root)

file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть', command=open_file)
file_menu.add_command(label='Сохранить', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Закрыть', command=notepad_exit)
root.config(menu=file_menu)

info_pro = Menu(main_menu, tearoff=0)
info_pro.add_command(label='info', command=info_prog)
root.config(menu=info_pro)


main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_cascade(label='info', menu=info_pro)
root.config(menu=main_menu)




f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

text_fild = Text(f_text,
                 bg='black',
                 fg='lime',
                 padx=5,
                 pady=5,
                 wrap=WORD,
                 insertbackground='brown',
                 selectbackground='#8D917A',
                 spacing3=10,
                 width=30,
                 font='Time_New_Roman 14 bold'
                 )
text_fild.pack(expand=1, fill=BOTH, side=LEFT)
scroll = Scrollbar(f_text, command=text_fild.yview)
scroll.pack(side = LEFT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)

root.mainloop()