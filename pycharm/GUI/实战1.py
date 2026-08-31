import tkinter
import tkinter as tk
from tkinter import messagebox

user_name_map={}
email_map={}

window=tk.Tk()
window.title("登录/注册界面")
window.geometry("500x500+100+100")
window.resizable(False,False)

label_1=tk.Label(window,text="账号:",font=("consolas",26),)
label_1.place(x=50,y=100)

label_2=tk.Label(window,text="密码:",font=("consolas",26),)
label_2.place(x=50,y=180)

str_1=tk.StringVar()
# str_1.set("请输入账号")
str_2=tk.StringVar()
# str_2.set("请输入密码")

entry_1=tk.Entry(window,textvariable=str_1,width=15,font=("consolas",26),)
entry_1.place(x=150,y=100)

entry_2=tk.Entry(window,textvariable=str_2,width=15,font=("consolas",26),)
entry_2.place(x=150,y=180)

def log_in():
    print(str_1.get()," ",str_2.get())
    if not str_1.get() or not str_2.get():
        messagebox.showinfo("错误","信息未填写")
    elif str_1.get()!="123" or str_2.get()!="123":
        choice=messagebox.askokcancel("错误","填写信息错误，请再次尝试")
        if not choice:
            window.destroy()
    else:
        window.destroy()

def register_in():
    new_window = tk.Toplevel()
    new_window.title("注册页面")
    new_window.geometry("400x400+100+100")
    new_window.resizable(False, False)

    user_name_str=tk.StringVar()
    email_str=tk.StringVar()
    password_str=tk.StringVar()
    confirm_psw_str=tk.StringVar()

    user_name_label=tk.Label(new_window,text="账号名:",font=("consolas",20))
    user_name_label.grid(row=1,column=1)
    email_label=tk.Label(new_window,text="邮箱:",font=("consolas",20))
    email_label.grid(row=2,column=1)
    password_label=tk.Label(new_window,text="密码:",font=("consolas",20))
    password_label.grid(row=3,column=1)
    confirm_psw_label=tk.Label(new_window,text="确认密码:",font=("consolas",20))
    confirm_psw_label.grid(row=4,column=1)

    user_name_entry=tk.Entry(new_window,textvariable=user_name_str,width=12,font=("consolas",26),)
    user_name_entry.grid(row=1,column=2)
    email_entry = tk.Entry(new_window,textvariable=email_str,width=12, font=("consolas", 26), )
    email_entry.grid(row=2, column=2)
    password_entry = tk.Entry(new_window,textvariable=password_str, width=12, font=("consolas", 26), )
    password_entry.grid(row=3, column=2)
    confirm_psw_entry = tk.Entry(new_window,textvariable=confirm_psw_str, width=12, font=("consolas", 26), )
    confirm_psw_entry.grid(row=4, column=2)

    def input_information():
        user_name=user_name_str.get()
        email=email_str.get()
        password=password_str.get()
        confirm_psw=confirm_psw_str.get()
        if not user_name or not email or not password or not confirm_psw:
            messagebox.showwarning("错误","信息缺失")
        elif password!=confirm_psw:
            messagebox.showwarning("错误","前后密码不一致")
        elif user_name_map[user_name]==1:
            messagebox.showwarning("错误","用户名重复")
        elif email_map[email]==1:
            messagebox.showwarning("错误","该邮箱已注册")
        else:
            user_name_map[user_name]=1
            email_map[email]=1
            choice=messagebox.showinfo("注册成功")

    register_in_button=tk.Button(new_window,text="注册",width=10,font=("consolas", 26),command=input_information)
    register_in_button.place(x=100,y=250)

button_1=tk.Button(window,text="登录",width=10,font=("consolas", 26),command=log_in)
button_1.place(x=50,y=280)

button_2=tk.Button(window,text="注册",width=10,font=("consolas", 26),command=register_in)
button_2.place(x=250,y=280)

def close_window():
    choice=messagebox.askokcancel("关闭窗口","是否关闭窗口")
    if choice:
        window.destroy()

# window.protocol("WM_DELETE_WINDOW",close_window())

window.mainloop()