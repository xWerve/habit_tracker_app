import tkinter as tk

root = tk.Tk()
root.title("Habit Tracker")
root.geometry('1400x600')

zmienna = tk.BooleanVar()
check = tk.Checkbutton(root, text='Nawyk 1', variable=zmienna).pack()

root.mainloop()
