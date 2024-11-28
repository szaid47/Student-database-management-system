from customtkinter import *
from PIL import Image

def create_main_window():
    root1 = CTk()
    root1.geometry('1024x600')
    root1.resizable(0, 0)
    root1.title('Choose Database')

    headinglabel = CTkLabel(root1, text='Select Database', bg_color='#232534', font=('Goudy Old Style', 25, 'bold'), text_color='white')
    headinglabel.place(x=450, y=100)

    def ems():
        root1.destroy()
        import ems

    def dms():
        root1.destroy()
        import dms

    emsFrame = CTkFrame(root1)
    emsFrame.place(x=200, y=300)

    emsButton = CTkButton(emsFrame, text='Employee Management System', width=200, command=ems)
    emsButton.pack(padx=10, pady=10)

    dmsFrame = CTkFrame(root1)
    dmsFrame.place(x=600, y=300)

    dmsButton = CTkButton(dmsFrame, text='Department Management System', width=200, command=dms)
    dmsButton.pack(padx=10, pady=10)

    root1.mainloop()

create_main_window()
