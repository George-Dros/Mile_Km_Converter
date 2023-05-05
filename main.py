from tkinter import *
from converter import Converter

def button_click():
    number = input.get()
    s_label.config(text=f"{Converter().miles_to_km(number)}")



window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=400, height=300)
window.config(padx=20,pady=20)


di_label = Label(text="Distance:", font=("Times New Roman", 17, "normal"))
di_label.grid(column=0, row=0)
di_label.config(padx=10, pady=20)

input = Entry(width=20)
input.grid(column=1,row=0)

mi_label = Label(text="Miles", font=("Times New Roman", 17, "normal"))
mi_label.grid(column=2, row=0)
mi_label.config(padx=10, pady=20)

e_label = Label(text="are equal to:", font=("Times New Roman", 17, "normal"))
e_label.grid(column=0, row=1)
e_label.config(padx=10, pady=20)

s_label = Label(text="0", font=("Times New Roman", 17, "normal"))
s_label.grid(column=1, row=1)
s_label.config(padx=10, pady=20)

u_label = Label(text="Km", font=("Times New Roman", 17, "normal"))
u_label.grid(column=2, row=1)
u_label.config(padx=10, pady=20)

button = Button(text="Calculate!",command=button_click,font=("Times New Roman", 15, "bold"))
button.config(height=2)
button.grid(column=1,row=2)

window.mainloop()