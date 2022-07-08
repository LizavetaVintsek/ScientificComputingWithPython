import tkinter as tk
import random

def random_number():
    value = int(label_value["text"])
    label_value["text"] = "{}".format(random.randint(1, 6))

root = tk.Tk()


root.rowconfigure(0, minsize=100, weight=1)
root.columnconfigure(0, minsize=100, weight=1)
root.columnconfigure(1, minsize=100, weight=1)
root.columnconfigure(2, minsize=100, weight=1)

label = tk.Label(root, text="Six-sided die simulator", bg="white", font="Times 16 bold")
label.grid(row=0, column=0)

button = tk.Button(root, text="Press", command=random_number)
button.grid(row=0, column=1, sticky=tk.NSEW)

label_value = tk.Label(root, text="0")
label_value.grid(row=0, column=2)


root.mainloop()
