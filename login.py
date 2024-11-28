from customtkinter import *
from PIL import Image
from tkinter import messagebox
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='' :
        messagebox.showerror('Error ', 'All fields are required')

    elif usernameEntry.get()=='zaheed' and passwordEntry.get()=='1234':
        messagebox.showinfo('success','welcome')
        root.destroy()
        import choice

    else:
        messagebox.showerror('Error ', 'wrong credentials')


root = CTk()
root.geometry('1024x600')
root.resizable(0,0)
root.title('login  page')
image = CTkImage(Image.open('coverf.jpg'),size=(1024,600))
imageLabel=CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)
headinglabel = CTkLabel(root,text= 'Database Management System',bg_color='#C5CCD2',font=('Goudy Old Style',25,'bold'),text_color='dark blue' )
headinglabel.place(x=40,y=100)

usernameEntry=CTkEntry(root,placeholder_text='enter your username',width=180)
usernameEntry.place(x=60,y=150)

passwordEntry=CTkEntry(root,placeholder_text='enter your password',width=180,show='*')
passwordEntry.place(x=60,y=200)

loginButton=CTkButton(root,text='login',cursor='hand2',command=login)
loginButton.place(x=70,y=250)

root.mainloop()