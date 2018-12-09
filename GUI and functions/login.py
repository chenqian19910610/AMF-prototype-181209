from tkinter import *

Winstat = ' '
def open_win():
    global application,Winstat
    Winstat = 'application'
    import unknown
    L1 = unknown.vp_start_gui()

def main_window():
    global username,pwd,Winstat,root,application
    if Winstat=='application':
        application.destroy()
    root=Tk()
    root.title('Login')
    root.wm_iconbitmap('logo.ico')
    root.configure(background='#e5eef4')

    Label(root,text='Username').grid(row=0,column=0)
    username=Entry(root,width=10)
    username.grid(row=0,column=1)
    Label(root, text='Password').grid(row=1, column=0)
    pwd = Entry(root, width=10, show='*')
    pwd.grid(row=1, column=1)
    Button(root,width=6, text='Login', command=checkpassword).grid(row=2,column=0)
    Button(root, width=6, text='Close', command=root.destroy).grid(row=2, column=1)

    root.resizable(width=True,height=False)

    root.mainloop()

def  checkpassword():
    global username,pwd,root
    u=username.get()
    p=pwd.get()
    if 'ibi'!=u or '1234'!=p:
        top=Tk()
        Label(top,width=30,text='wrong username or password').grid(row=0,column=0)
        # top.destroy()
        top.mainloop()
    else:
        root.destroy()
        open_win()


main_window()
