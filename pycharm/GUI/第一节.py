import tkinter as tk

window=tk.Tk()
window.title("my_window")
window.geometry("200x100")

label=tk.Label(
    window,text="Label",
    bg="green",
    font=("Arial",12),
    width=15,
    height=2
    )
label.pack()

window.mainloop()
