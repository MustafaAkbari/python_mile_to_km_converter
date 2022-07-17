from tkinter import *
from tkinter import messagebox


def mile_to_km():
    """
    A function that convert mile to km, it takes the value of mile from entry, after performing math calculation,
    pars the result to the label
    :return:
    """
    try:
        mile = entry.get()
        km = float(mile) * 1.60934
        label_3.config(text=round(km, 2))
    except ValueError:
        messagebox.showerror("Wrong Value", "Please enter an integer or float datatype")
    finally:
        entry.delete(0, "end")


# creating screen
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20, bg="gray")

# creating entry
entry = Entry(font=("arial", 10, "bold"))
entry.grid(column=1, row=0)

# creating 4 label
label_1 = Label(text=" :Miles")
label_1.grid(column=2, row=0)
label_1.config(bg="gray")
label_2 = Label(text="Is equal to: ")
label_2.grid(column=0, row=1)
label_2.config(bg="gray")
label_3 = Label(text=0)
label_3.grid(column=1, row=1)
label_3.config(bg="gray")
label_4 = Label(text="Km")
label_4.grid(column=2, row=1)
label_4.config(bg="gray")

# creating button that convert mile to km
button = Button(text="Convert", command=mile_to_km)
button.grid(column=1, row=2)

window.mainloop()
