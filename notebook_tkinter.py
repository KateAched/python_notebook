from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

def chenge_theme(theme):
    text_fild['bg'] = view_colors[theme]['text_bg']
    text_fild['fg'] = view_colors[theme]['text_fg']
    text_fild['insertbackground'] = view_colors[theme]['cursor']
    text_fild['selectbackground'] = view_colors[theme]['select_bg']

def chenge_fonts(fontss):
    text_fild['font'] = fonts[fontss]['font']

def notepad_exit():
    answer = messagebox.askokcancel('Выход', 'Вы точно хотите выйти?')
    if answer:
        root.destroy()

def open_file():
    file_path=filedialog.askopenfilename(title='Выбор файлов', filetypes=(('Текстовые документы (*.txt)', '*,txt'), ('Все файлы', '*.*')))
    if file_path:
        text_fild.delete('1.0', END)
        text_fild.insert('1.0', open(file_path, encoding='utf-8').read())

def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы (*.txt)', '*,txt'), ('Все файлы', '*.*')))
    f=open(file_path, 'w', encoding='utf-8')
    text=text_fild.get('1.0', END)
    f.write(text)
    f.close()

root = Tk()
root.title('Текстовый редактор')
root.geometry('600x800')

main_menu = Menu(root)

#Файл
file_menu= Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть', command=open_file)
file_menu.add_separator()
file_menu.add_command(label='Сохранить', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Закрыть', command=notepad_exit)
root.config(menu=file_menu)

#ВИД
view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
fond_menu_sub = Menu(view_menu, tearoff= 0)
view_menu_sub.add_command(label='Тёмная тема', command=lambda: chenge_theme('dark'))
view_menu_sub.add_command(label='Светлая тема', command=lambda: chenge_theme('light'))
view_menu.add_cascade(label='Тема', menu=view_menu_sub)

fond_menu_sub.add_command(label='Arial', command=lambda: chenge_fonts('Arial'))
fond_menu_sub.add_command(label='Comic Sans MS', command=lambda: chenge_fonts('CSMS'))
fond_menu_sub.add_command(label='Times New Roman', command=lambda: chenge_fonts('TNR'))
view_menu.add_cascade(label='Шрифт', menu=fond_menu_sub)
root.config(menu=view_menu)


#Добавление списков меню
main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_cascade(label='Вид', menu=view_menu)
root.config(menu=main_menu)


f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

view_colors = {
    'dark' : {
        'text_bg': 'black', 'text_fg' : 'pink', 'cursor' : 'brown', 'select_bg' : '#FA8072'
    },
    'light': {
        'text_bg': 'white', 'text_fg' : 'blue', 'cursor' : '#9966CC', 'select_bg' : 'Gray'
    }
}
fonts = {
    'Arial' : {
        'font': 'Arial 14 bold'
    },
    'CSMS': {
        'font': ('Comic Sans MS', 14, 'bold')
    },
    'TNR': {
        'font': ('Times New Roman', 14, 'bold')
    }
}

text_fild = Text(f_text,
                 bg='black',
                 fg='pink',
                 padx=10,
                 pady = 10,
                 wrap= WORD,
                 insertbackground='brown',
                 selectbackground='#FA8072',
                 spacing3=10,
                 font=14,
                 )

text_fild.pack(expand=1, fill=BOTH, side='left')

scroll=Scrollbar(f_text, command=text_fild.yview)
scroll.pack(side=LEFT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)


root.mainloop()