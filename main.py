# Version 2.0


from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import fileinput



def _open():
    op = askopenfilename()
    print(op)
    f = open(op, "r", encoding='utf-8')
    content = f.read()
    txt.delete(1.0, END)
    txt.insert(END, content)
    f.close()


def _save():
    sa = asksaveasfilename()
    content = txt.get(1.0, END)
    f = open(sa, "w", encoding='utf-8')
    f.write(content)
    f.close()


def close_win():
    if askyesno(title="Выход", message="Вы уверены?"):
        root.destroy()


def about():
    showinfo(title="Редактор", message="Простейший текстовый редактор")


root = Tk()

m = Menu(root)
root.config(menu=m)

fm = Menu(m)
m.add_cascade(label="Файл", menu=fm)
fm.add_command(label="Открыть...", command=_open)
fm.add_command(label="Сохранить как...", command=_save)
fm.add_command(label="Выход", command=close_win)

hm = Menu(m)
m.add_cascade(label="Справка", menu=hm)
hm.add_command(label="О программе", command=about)

txt = Text(root, width=40, height=15, font=('times', 12))
txt.pack()

txt.insert(1.0, "empty")
root.mainloop()
