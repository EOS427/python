import tkinter as tk

window=tk.Tk()
window.title("new window")
window.geometry("500x500+100+100")
window.resizable(True,True)

label_1=tk.Label(window,
                 text="账号:",
                 font=("consolas",26),
                 )
label_1.place(x=50,y=100)

label_2=tk.Label(window,
                 text="密码:",
                 font=("consolas",26),
                 )
label_2.place(x=50,y=180)

str_1=tk.StringVar()
# str_1.set("请输入账号")
str_2=tk.StringVar()
# str_2.set("请输入密码")

entry_1=tk.Entry(window,
         textvariable=str_1,
         width=15,
         font=("consolas",26),
         )
entry_1.place(x=150,y=100)

entry_2=tk.Entry(window,
         textvariable=str_2,
         width=15,
         font=("consolas",26),
         )
entry_2.place(x=150,y=180)

def log_in():
    print(str_1.get()," ",str_2.get())
    window.destroy()


button_1=tk.Button(window,
                   text="登录",
                   width=10,
                   font=("consolas", 26),
                   command=log_in
                   )
button_1.place(x=140,y=280)


window.mainloop()