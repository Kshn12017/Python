import tkinter as tk

def clear_result():
    entry3.config(text="")

def add():
    clear_result()
    try:
        v1 = float(entry1.get())
        v2 = float(entry2.get())
        result = v1 + v2
    except ValueError:
        result = "Invalid input"
    entry3.config(text=result)
    
def sub():
    clear_result()
    try:
        v1 = float(entry1.get())
        v2 = float(entry2.get())
        result = v1 - v2
    except ValueError:
        result = "Invalid input"
    entry3.config(text=result)

def mul():
    clear_result()
    try:
        v1 = float(entry1.get())
        v2 = float(entry2.get())
        result = v1 * v2
    except ValueError:
        result = "Invalid input"
    entry3.config(text=result)

def div():
    clear_result()
    try:
        v1 = float(entry1.get())
        v2 = float(entry2.get())
        if v2 == 0:
            result = "Error: Div by 0"
        else:
            result = v1 / v2
    except ValueError:
        result = "Invalid input"
    entry3.config(text=result)

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(210, 100, window=entry1)

entry2 = tk.Entry(root)
canvas1.create_window(210, 140, window=entry2)

entry3 = tk.Label(root, text="", font=('helvetica', 10, 'bold'), bg='white')
canvas1.create_window(210, 240, window=entry3)

label0 = tk.Label(root, text='Calculator')
label0.config(font=('helvetica', 14))
canvas1.create_window(150, 40, window=label0)

label1 = tk.Label(root, text='Type Value 1:')
label1.config(font=('helvetica', 10))
canvas1.create_window(100, 100, window=label1)

label2 = tk.Label(root, text='Type Value 2:')
label2.config(font=('helvetica', 10))
canvas1.create_window(100, 140, window=label2)

label3 = tk.Label(root, text='Result:')
label3.config(font=('helvetica', 10))
canvas1.create_window(100, 240, window=label3)

buttonAdd = tk.Button(text='+', command=add, bg='green', fg='white', font=('helvetica', 9, 'bold'), width=5)
canvas1.create_window(90, 190, window=buttonAdd)

buttonSub = tk.Button(text='–', command=sub, bg='green', fg='white', font=('helvetica', 9, 'bold'), width=5)
canvas1.create_window(140, 190, window=buttonSub)

buttonMul = tk.Button(text='x', command=mul, bg='green', fg='white', font=('helvetica', 9, 'bold'), width=5)
canvas1.create_window(190, 190, window=buttonMul)

buttonDiv = tk.Button(text='/', command=div, bg='green', fg='white', font=('helvetica', 9, 'bold'), width=5)
canvas1.create_window(240, 190, window=buttonDiv)

root.mainloop()