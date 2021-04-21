from tkinter import *
from tkinter import ttk

c = """c=3e8
R=8.314
k=1.38e-23
I_0=1e-12
g_z=9.81"""

constants_list = [i.split("=")[0] for i in c.split()]


def open_constants():
    global const_check
    global window_constants
    window_constants = Tk()
    info = Label(master = window_constants, text = "Odaberi relevantne konstante za zadatak.")
    info.pack()
    const_check = {}
    for i in constants_list:
        const_check[i] = ttk.Checkbutton(master = window_constants, text = i)
        const_check[i].state(['!alternate'])
        const_check[i].state(['!selected'])
        const_check[i].pack()
    constants_accept = Button(master = window_constants, text = "Prihvati", command = send)
    constants_accept.pack()
    
def send():
    for key, value in const_check.items():
        print(key, value.instate(['selected']))
    window_constants.destroy()
    return

window = Tk()
constants = Button(text = "konstante", command = open_constants)
constants.pack()



"""
window = Tk()
const_check = {}
for i in consts:
    const_check[i] = ttk.Checkbutton(text = i)
    const_check[i].state(['!alternate'])
    const_check[i].state(['!selected'])
    const_check[i].pack()
b = Button(text = "Send", command = send)
b.pack()

"""

"""window = tk.Tk()
window.title("Generator zadataka")
label = tk.Label(text = "Unesi tekst zadatka:", font = ("Calibri", 12))
label2 = tk.Label(text = "Veličine upiši u vitičaste zagrade.", font = ("Calibri", 8))
entry = tk.Entry()
button = tk.Button(text = "Save")
button2 = tk.Button(text = "Save and more")


from tkinter.ttk import *
from tkinter import *
dropdown = Combobox()
dropdown['values'] = ("a", "b", "c", "d")
dropdown.current(1)

ch_state = BooleanVar()
ch_state.set(False)
check = Checkbutton(text = "Choose", var=ch_state)

label.grid(column = 1, row = 0, columnspan = 3, sticky = "W")
label2.grid(column = 1, row = 1, columnspan = 3, sticky = "W")
entry.grid(column = 1, row = 2, columnspan = 3, sticky = "W")
button.grid(column = 1, row = 3, sticky = "W")
button2.grid(column = 2, row = 3, sticky = "W")
dropdown.grid(row = 5, column = 1, columnspan = 2)
check.grid(row = 6, column = 1)

rad1 = Radiobutton(window,text='First', value=1)
rad2 = Radiobutton(window,text='Second', value=2)
rad3 = Radiobutton(window,text='Third', value=3)
rad1.grid(column=0, row=7)
rad2.grid(column=1, row=7)
rad3.grid(column=2, row=7)

window.update()
w = window.winfo_reqwidth()
print(w)
h = window.winfo_reqheight()
print(h)
dim = "{}x{}".format(w + 100, h + 100)
window.geometry(dim) # width x height


def click1():
    label.configure(text = "1")
    return

def click2():
    label.configure(text = "2")
    return

def show():
    window = tk.Tk()
    label = tk.Label(text = "Text")
    button1 = tk.Button(text = "1", command=click1)
    button2 = tk.Button(text = "2", command=click2)

    label.grid(row = 0, column = 0, columnspan = 2)
    button1.grid(row = 1, column = 0)
    button2.grid(row = 1, column = 1)

"""

"""
master=tk.Tk()
master.title("place() method")
master.geometry("450x350")

button1=tk.Button(master, text="button1")
button1.place(x=25, y=100)

button2=tk.Button(master, text="button2")
button2.place(x=100, y=25)

button3=tk.Button(master, text="button3")
button3.place(x=175, y=100)

master.mainloop()
"""



