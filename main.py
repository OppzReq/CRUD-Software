from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import askyesno
import sqlite3
import time

time_object = time.localtime()
submit_counter = 0

conn = sqlite3.connect("customers.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS customer_table(customer_information TEXT)""")
c.execute("SELECT * FROM customer_table")
conn.commit()

data = c.fetchall()

window = Tk()
window.title("CRUD software")
window.geometry("750x213")
window.resizable(width=False, height=False)

def submit():
    if input_name.get() == "" or input_phone.get() == "" or input_address.get() == "":
        messagebox.showerror(title="Error",
                             message="Make sure to fill each section and try again")

    else:
        global submit_counter
        submit_counter += 1
        input_name_text = input_name.get()
        input_phone_text = input_phone.get()
        input_address_text = input_address.get()

        insert_info = input_name_text + " | " + input_phone_text + " | " + input_address_text + " | " + time.strftime("%c",time_object)

        conn = sqlite3.connect("customers.db")
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS customer_table(customer_information TEXT)""")
        c.execute("INSERT INTO customer_table VALUES ('" + insert_info + "')")
        conn.commit()

        listbox.insert(submit_counter, insert_info)

        input_name.delete(0, END)
        input_phone.delete(0, END)
        input_address.delete(0, END)


def delete():

    delete_info = ""

    for i in listbox.curselection():
        delete_info += listbox.get(i)

    delete_answer = askyesno(title="Confirm",
                             message=f"Are you sure you want to delete {delete_info}?")

    if delete_answer:
        conn = sqlite3.connect("customers.db")
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS customer_table(customer_information TEXT)""")
        c.execute("DELETE FROM customer_table WHERE customer_information='" + delete_info + "'")
        conn.commit()

        listbox.delete(listbox.curselection())
    else:
        pass

def update():
    if input_name.get() == "" or input_phone.get() == "" or input_address.get() == "":
        messagebox.showerror(title="Error",
                             message="To update/change an item, right click it to select, then fill in the fields with your updated information")
    else:

        old_info = ""

        for i in listbox.curselection():
            old_info += listbox.get(i)

        change_answer = askyesno(title="Confirm",
                                 message=f"Are you sure you would like to change {old_info}?")
        if change_answer:

            conn = sqlite3.connect("customers.db")
            c = conn.cursor()

            c.execute("""CREATE TABLE IF NOT EXISTS customer_table(customer_information TEXT)""")
            c.execute("DELETE FROM customer_table WHERE customer_information='" + old_info + "'")
            conn.commit()

            listbox.delete(listbox.curselection())


            global submit_counter
            submit_counter += 1
            input_name_text = input_name.get()
            input_phone_text = input_phone.get()
            input_address_text = input_address.get()

            insert_info = input_name_text + " | " + input_phone_text + " | " + input_address_text + " | " + time.strftime("%c",time_object)

            conn = sqlite3.connect("customers.db")
            c = conn.cursor()

            c.execute("""CREATE TABLE IF NOT EXISTS customer_table(customer_information TEXT)""")
            c.execute("INSERT INTO customer_table VALUES ('" + insert_info + "')")
            conn.commit()

            listbox.insert(submit_counter, insert_info)

            input_name.delete(0, END)
            input_phone.delete(0, END)
            input_address.delete(0, END)
        else:
            pass

def get():
    get_temp = ""

    for i in listbox.curselection():
        get_temp += listbox.get(i)

    part_get = get_temp.split(" | ")

    input_name.delete(0, END)
    input_phone.delete(0, END)
    input_address.delete(0, END)

    input_name.insert(0, part_get[0])
    input_phone.insert(0, part_get[1])
    input_address.insert(0, part_get[2])

def show():
    show_temp = ""
    for i in listbox.curselection():
        show_temp += listbox.get(i)

    show = messagebox.showinfo(title="Information",
                               message=f"{show_temp}")

over_listbox_name = Label(window,
                          text="Name | Phone | Address | Date",
                          font=("consola", 8))


label_name = Label(window,
              text="Name:",
              font=("arial", 12))

label_phone = Label(window,
              text="Phone Number:",
              font=("arial", 12))

label_address = Label(window,
              text="Address:",
              font=("arial", 12))

input_name = Entry(window,
              font=("consola", 10))

input_phone = Entry(window,
              font=("consola", 10))

input_address = Entry(window,
              font=("consola", 10))


submit_button = Button(window,
                       text="Submit",
                       width=31,
                       height=1,
                       fg = "green",
                       activeforeground = "green",
                       command=submit)

delete_button = Button(window,
                       text="Delete",
                       width=17,
                       height=1,
                       fg = "red",
                       activeforeground = "red",
                       command=delete)

update_button = Button(window,
                       text="Update",
                       width=17,
                       height=1,
                       fg = "dark orange",
                       activeforeground = "orange",
                       command=update)

get_button = Button(window,
                       text="Get",
                       width=10,
                       height=1,
                       fg = "Black",
                       activeforeground = "Black",
                       command=get)

show_button = Button(window,
                       text="Show Full",
                       width=10,
                       height=1,
                       fg = "Black",
                       activeforeground = "Black",
                       command=show)

listbox = Listbox(window,
                  width=62,
                  height=13,
                  font=("consola", 8))

c.execute("SELECT * FROM customer_table")
var = c.fetchall()
conn.commit()

for i in var:
    listbox.insert(submit_counter, i[0])

label_name.place(x = 14, y = 17)
input_name.place(x = 130, y = 17)

label_phone.place(x = 14, y = 37)
input_phone.place(x = 130, y = 37)

label_address.place(x = 14, y = 57)
input_address.place(x = 130, y = 57)

submit_button.place(x = 14, y = 168)
delete_button.place(x = 126, y = 134)
update_button.place(x = 126, y = 100)
get_button.place(x = 14, y = 100)
show_button.place(x = 14, y = 134)

listbox.place(x = 300, y = 15)

over_listbox_name.place(x = 300, y = 0)


window.mainloop()
