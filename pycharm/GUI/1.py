import tkinter as tk
from PIL import Image,ImageTk

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

window.resizable(False,False)

image=Image.open("D:\桌面\Pictures\微信图片_20260126212102_182_276.jpg")
icon=ImageTk.PhotoImage(image)
window.iconphoto(True,icon)

def close_window():
    print("关闭窗口")

window.configure(bg='purple')
window.attributes('-alpha',1)
window.attributes('-topmost',True)
window.protocol('WM_DELETE_WINDOW',close_window)

window.mainloop()
