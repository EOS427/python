import tkinter as tk

window=tk.Tk()
window.title("new window")
win_size=["300","300"]
# window.geometry('x'.join(win_size))
window.update_idletasks()

scr_half_height=window.maxsize()[1]//2
scr_half_width=window.maxsize()[0]//2

# win_half_height=window.winfo_height()//2
# win_half_width=window.winfo_width()//2

win_half_height=int(win_size[0])//2
win_half_width=int(win_size[1])//2

x_coor=scr_half_width-win_half_width
y_coor=scr_half_height-win_half_height

window.geometry('x'.join(win_size)+f"+{x_coor}+{y_coor}")

window.geometry()
window.mainloop()
