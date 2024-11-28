from customtkinter import *
from tkinter import ttk, messagebox
import database
import choice

window = CTk()
window.geometry('1300x600+100+100')
window.resizable(0, 0)
window.title('Employee Management System')

def back():
    window.destroy()
    choice.create_main_window()


def delete_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error', 'Select data to delete')
    else:
        emp_id = idEntry.get()
        if not emp_id:
            messagebox.showerror('Error', 'No employee ID selected')
            return
        database.delete(emp_id)
        treeview_data()
        clear()


def showall():
    treeview_data()
    searchEntry.delete(0, END)
    searchbox.set('Search by')


def search_employee():
    search_text = searchEntry.get()
    search_option = searchbox.get()
    if not search_text:
        messagebox.showerror('Error', 'Enter search text')
        return
    if not search_option:
        messagebox.showerror('Error', 'Select search option')
        return

    searched_data = database.search(search_option, search_text)
    if not searched_data:
        messagebox.showinfo('Info', 'No matching records found')
    else:
        tree.delete(*tree.get_children())
        for employee in searched_data:
            tree.insert('', END, values=employee)


def treeview_data():
    try:
        employees = database.fetch_employees()
        tree.delete(*tree.get_children())
        for employee in employees:
            tree.insert('', END, values=employee)
    except Exception as e:
        messagebox.showerror('Error', f'Failed to fetch data: {str(e)}')


def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    roleBox.set('Lecturer/Instructor')
    genderBox.set('Male')
    salaryEntry.delete(0, END)
    deptEntry.delete(0, END)


def selection(event):
    selected_item = tree.selection()
    clear()
    if selected_item:
        row = tree.item(selected_item)['values']
        idEntry.insert(0, row[0])
        nameEntry.insert(0, row[1])
        phoneEntry.insert(0, row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0, row[5])
        deptEntry.insert(0, row[6])


def update_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error', 'Select data to update')
    else:
        emp_id = idEntry.get()
        if not emp_id:
            messagebox.showerror('Error', 'No employee ID selected')
            return
        database.update(emp_id, nameEntry.get(), phoneEntry.get(), roleBox.get(), genderBox.get(), salaryEntry.get(),
                        deptEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success', 'Data updated successfully')


def add_employee():
    emp_id = idEntry.get()
    emp_name = nameEntry.get()
    phone = phoneEntry.get()
    role = roleBox.get()
    gender = genderBox.get()
    salary = salaryEntry.get()
    dept_id = deptEntry.get()

    if not all([emp_id, emp_name, phone, role, gender, salary, dept_id]):
        messagebox.showerror('Error', 'All fields are required')
        return

    if database.id_exists(emp_id):
        messagebox.showerror('Error', 'Employee ID already exists')
        return

    try:
        database.insert(emp_id, emp_name, phone, role, gender, salary, dept_id)
        treeview_data()
        clear()
        messagebox.showinfo('Success', 'Employee added successfully')
    except Exception as e:
        messagebox.showerror('Error', f'Failed to add employee: {str(e)}')


def deleteall():
    response = messagebox.askyesnocancel("Confirm Delete All", "Do you really want to delete all records?")
    if response:
        try:
            database.deleteall()
            treeview_data()
            messagebox.showinfo('Success', 'All records deleted successfully')
        except Exception as e:
            messagebox.showerror('Error', f'Failed to delete all records: {str(e)}')


leftFrame = CTkFrame(window)
leftFrame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

idLabel = CTkLabel(leftFrame, text='ID', font=('arial', 18, 'bold'))
idLabel.grid(row=0, column=0, padx=20, pady=15, sticky='w')

idEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180, fg_color='white', text_color='black')
idEntry.grid(row=0, column=1)

nameLabel = CTkLabel(leftFrame, text='Name', font=('arial', 18, 'bold'))
nameLabel.grid(row=1, column=0, padx=20, pady=15, sticky='w')

nameEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180, fg_color='white', text_color='black')
nameEntry.grid(row=1, column=1)

phoneLabel = CTkLabel(leftFrame, text='Phone', font=('arial', 18, 'bold'))
phoneLabel.grid(row=2, column=0, padx=20, pady=15, sticky='w')

phoneEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180, fg_color='white', text_color='black')
phoneEntry.grid(row=2, column=1)

roleLabel = CTkLabel(leftFrame, text='Role', font=('arial', 18, 'bold'))
roleLabel.grid(row=3, column=0, padx=20, pady=15, sticky='w')

deptLabel = CTkLabel(leftFrame, text='Dept ID', font=('arial', 18, 'bold'))
deptLabel.grid(row=6, column=0, padx=20, pady=15, sticky='w')

deptEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180, fg_color='white', text_color='black')
deptEntry.grid(row=6, column=1)

role_options = [
    "Dean of Engineering", "Department Chair/Head", "Professor", "Associate Professor",
    "Assistant Professor", "Lecturer/Instructor", "Adjunct Professor", "Research Scientist/Engineer",
    "Postdoctoral Researcher", "Teaching Assistant (TA)", "Lab Instructor/Coordinator", "Academic Advisor"
]

roleBox = CTkComboBox(leftFrame, values=role_options, width=180, font=('arial', 15, 'bold'), state='readonly',
                      fg_color='white', text_color='black')
roleBox.grid(row=3, column=1)
roleBox.set(role_options[5])

genderLabel = CTkLabel(leftFrame, text='Gender', font=('arial', 18, 'bold'))
genderLabel.grid(row=4, column=0, padx=20, pady=15, sticky='w')

gender_option = ['Male', 'Female']
genderBox = CTkComboBox(leftFrame, values=gender_option, width=180, font=('arial', 15, 'bold'), state='readonly',
                        fg_color='white', text_color='black')
genderBox.grid(row=4, column=1)
genderBox.set(gender_option[0])

salaryLabel = CTkLabel(leftFrame, text='Salary', font=('arial', 18, 'bold'))
salaryLabel.grid(row=5, column=0, padx=20, pady=15, sticky='w')

salaryEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180, fg_color='white', text_color='black')
salaryEntry.grid(row=5, column=1)

rightFrame = CTkFrame(window)
rightFrame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

search_option = ['ID', 'Name', 'Phone', 'Role', "Gender", 'Salary']
searchbox = CTkComboBox(rightFrame, values=search_option, width=180, font=('arial', 15, 'bold'), state='readonly',
                        fg_color='white', text_color='black')
searchbox.grid(row=0, column=0)
searchbox.set('Search by')

searchEntry = CTkEntry(rightFrame, fg_color='white', font=('arial', 12, 'bold'))
searchEntry.grid(row=0, column=1)

searchButton = CTkButton(rightFrame, text='Search', width=100, command=search_employee)
searchButton.grid(row=0, column=2)

showallButton = CTkButton(rightFrame, text='Show All', width=100, command=showall)
showallButton.grid(row=0, column=3, pady=15)

tree = ttk.Treeview(rightFrame, height=13)
tree.grid(row=1, column=0, columnspan=4)

tree['column'] = ('id', 'name', 'phone', 'role', 'gender', 'salary', 'dept_id')
tree.heading('id', text='ID')
tree.heading('name', text='Name')
tree.heading('phone', text='Phone')
tree.heading('role', text='Role')
tree.heading('gender', text='Gender')
tree.heading('salary', text='Salary')
tree.heading('dept_id', text='Dept ID')

tree.config(show='headings')
tree.column('id', anchor=CENTER, width=100)
tree.column('name', anchor=CENTER, width=160)
tree.column('phone', anchor=CENTER, width=160)
tree.column('role', anchor=CENTER, width=200)
tree.column('gender', anchor=CENTER, width=100)
tree.column('salary', anchor=CENTER, width=140)
tree.column('dept_id', anchor=CENTER, width=100)

style = ttk.Style()
style.configure('Treeview.Heading', font=('Arial', 18, 'bold'))
style.configure('Treeview', font=('arial', 12, 'bold'), rowheight=30, background='#161c30', foreground='white')

scrollbar = ttk.Scrollbar(rightFrame, orient=VERTICAL, command=tree.yview)
scrollbar.grid(row=1, column=4, sticky='ns')

tree.config(yscrollcommand=scrollbar.set)

buttonFrame = CTkFrame(window)
buttonFrame.grid(row=2, column=0, columnspan=2, pady=10)

newButton = CTkButton(buttonFrame, text='New Employee', font=('arial', 15, 'bold'), width=160, corner_radius=15,
                      command=lambda: clear(True))
newButton.grid(row=0, column=0, pady=5, padx=5)

addButton = CTkButton(buttonFrame, text='Add Employee', font=('arial', 15, 'bold'), width=160, corner_radius=15,
                      command=add_employee)
addButton.grid(row=0, column=1, pady=5, padx=5)

updateButton = CTkButton(buttonFrame, text='Update Employee', font=('arial', 15, 'bold'), width=160, corner_radius=15,
                         command=update_employee)
updateButton.grid(row=0, column=2, pady=5, padx=5)

deleteButton = CTkButton(buttonFrame, text='Delete Employee', font=('arial', 15, 'bold'), width=160, corner_radius=15,
                         command=delete_employee)
deleteButton.grid(row=0, column=3, pady=5, padx=5)

deleteallButton = CTkButton(buttonFrame, text='Delete All', font=('arial', 15, 'bold'), width=160, corner_radius=15,
                            command=deleteall)
deleteallButton.grid(row=0, column=4, pady=5, padx=5)

exitButton = CTkButton(buttonFrame, text='Exit', font=('arial', 15, 'bold'), width=160, corner_radius=15,
                       command=window.quit)
exitButton.grid(row=0, column=5, pady=5, padx=5)

backButton = CTkButton(buttonFrame, text='back', font=('arial', 15, 'bold'), width=160, corner_radius=15,
                       command=back)
backButton.grid(row=0, column=6, pady=5, padx=5)


tree.bind('<<TreeviewSelect>>', selection)

treeview_data()

window.mainloop()
