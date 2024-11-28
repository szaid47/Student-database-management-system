from customtkinter import *
from tkinter import ttk, messagebox
import database
import choice

window = CTk()
window.geometry('1250x600+100+100')
window.resizable(0, 0)
window.title('Department Management System')

def back():
    window.destroy()
    choice.create_main_window()


def delete_department():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error', 'Select data to delete')
    else:
        database.dept_delete(idEntry.get())  # Assuming delete function exists in database module
        treeview_data()
        clear()

def show_all():
    treeview_data()
    searchEntry.delete(0, END)
    searchbox.set('Search by')

def search_department():
    if searchEntry.get() == '':
        messagebox.showerror('Error', 'Select an entry to search')
    elif searchbox.get() == '':
        messagebox.showerror('Error', 'Select an option to search')
    else:
        searched_data = database.search_dept(searchbox.get(), searchEntry.get())  # Assuming search function exists
        tree.delete(*tree.get_children())
        for dept in searched_data:
            tree.insert('', END, values=dept)

# Functions
def treeview_data():
    departments = database.fetch_departments()  # Assuming fetch_departments function exists
    tree.delete(*tree.get_children())
    for dept in departments:
        tree.insert('', END, values=dept)

def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0, END)
    deptNameEntry.delete(0, END)

def selection(event):
    selected_item = tree.selection()
    clear()
    if selected_item:
        row = tree.item(selected_item)['values']
        idEntry.insert(0, row[0])
        deptNameEntry.insert(0, row[1])

def update_department():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error', 'Select data to update')
    else:
        database.update_dept(idEntry.get(), deptNameEntry.get())  # Assuming update function exists
        treeview_data()
        clear()
        messagebox.showinfo('Success', 'Data is updated')

def add_department():
    if idEntry.get() == '' or deptNameEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    elif database.dept_id_exists(idEntry.get()):  # Assuming id_exists function exists
        messagebox.showerror('Error', 'ID already exists')
    else:
        database.dept_insert(idEntry.get(), deptNameEntry.get())  # Assuming insert function exists
        treeview_data()
        clear()
        messagebox.showinfo('Success', 'Data is added')

def delete_all():
    response = messagebox.askyesnocancel('Confirm Delete All', 'Do you really want to delete all records?')
    if response is None:
        return
    elif response:
        database.delete_all()  # Assuming delete_all function exists
        treeview_data()

leftFrame = CTkFrame(window)
leftFrame.grid(row=0, column=0, padx=10, pady=10)

idLabel = CTkLabel(leftFrame, text='ID', font=('Arial', 18, 'bold'))
idLabel.grid(row=0, column=0, padx=20, pady=15, sticky='w')

idEntry = CTkEntry(leftFrame, font=('Arial', 15, 'bold'), width=180, fg_color='white', text_color='black')
idEntry.grid(row=0, column=1)

deptNameLabel = CTkLabel(leftFrame, text='Department Name', font=('Arial', 18, 'bold'))
deptNameLabel.grid(row=1, column=0, padx=20, pady=15, sticky='w')

deptNameEntry = CTkEntry(leftFrame, font=('Arial', 15, 'bold'), width=180, fg_color='white', text_color='black')
deptNameEntry.grid(row=1, column=1)

rightFrame = CTkFrame(window)
rightFrame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

search_option = ['Dept_id', 'Dept_Name']
searchbox = CTkComboBox(rightFrame, values=search_option, width=180, font=('Arial', 15, 'bold'), state='readonly', fg_color='white', text_color='black')
searchbox.grid(row=0, column=0)
searchbox.set('Search by')

searchEntry = CTkEntry(rightFrame, fg_color='white')
searchEntry.grid(row=0, column=1)

searchButton = CTkButton(rightFrame, text='Search', width=100, command=search_department)
searchButton.grid(row=0, column=2)

showAllButton = CTkButton(rightFrame, text='Show All', width=100, command=show_all)
showAllButton.grid(row=0, column=3, pady=15)

tree = ttk.Treeview(rightFrame, height=13)
tree.grid(row=1, column=0, columnspan=4)

tree['columns'] = ('id', 'dept_name')
tree.heading('id', text='ID')
tree.heading('dept_name', text='Department Name')

tree.config(show='headings')
tree.column('id', anchor=CENTER, width=100)
tree.column('dept_name', anchor=CENTER, width=400)

style = ttk.Style()
style.configure('Treeview.Heading', font=('Arial', 18, 'bold'))
style.configure('Treeview', font=('Arial', 15, 'bold'), rowheight=30, background='#161c30', foreground='white')

scrollbar = ttk.Scrollbar(rightFrame, orient=VERTICAL, command=tree.yview)
scrollbar.grid(row=1, column=4, sticky='ns')

tree.config(yscrollcommand=scrollbar.set)

buttonFrame = CTkFrame(window)
buttonFrame.grid(row=2, column=0, columnspan=2, pady=10)

newButton = CTkButton(buttonFrame, text='New Department', font=('Arial', 15, 'bold'), width=160, corner_radius=15, command=lambda: clear(True))
newButton.grid(row=0, column=0, pady=5)

addButton = CTkButton(buttonFrame, text='Add Department', font=('Arial', 15, 'bold'), width=160, corner_radius=15, command=add_department)
addButton.grid(row=0, column=1, pady=5, padx=5)

updateButton = CTkButton(buttonFrame, text='Update Department', font=('Arial', 15, 'bold'), width=160, corner_radius=15, command=update_department)
updateButton.grid(row=0, column=2, pady=5, padx=5)

deleteButton = CTkButton(buttonFrame, text='Delete Department', font=('Arial', 15, 'bold'), width=160, corner_radius=15, command=delete_department)
deleteButton.grid(row=0, column=3, pady=5, padx=5)

deleteAllButton = CTkButton(buttonFrame, text='Delete All', font=('Arial', 15, 'bold'), width=160, corner_radius=15, command=delete_all)
deleteAllButton.grid(row=0, column=4, pady=5, padx=5)

exitButton = CTkButton(buttonFrame, text='Exit', font=('arial', 15, 'bold'), width=160, corner_radius=15,
                       command=window.quit)
exitButton.grid(row=0, column=5, pady=5, padx=5)

backButton = CTkButton(buttonFrame, text='back', font=('arial', 15, 'bold'), width=160, corner_radius=15,
                       command=back)
backButton.grid(row=0, column=6, pady=5, padx=5)

treeview_data()

window.bind('<<TreeviewSelect>>', selection)
window.mainloop()
