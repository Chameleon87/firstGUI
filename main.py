#!/usr/bin/python
from Tkinter import mainloop, Tk, Label, Button, Entry, Menu

root = Tk()


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Address+")

        self.label = Label(master, text="Welcome to Address Plus!")
        self.label.pack()

        self.new_contact_button = Button(master, text="Add Contact", command=self.new_contact)
        self.new_contact_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def new_contact(self):
        self.first_name_label = Label(master=None, text="First Name:")
        self.first_name_label.pack()

        self.first_name_entry = Entry(master=None)
        self.first_name_entry.pack()

        self.last_name_label = Label(master=None, text="Last Name:")
        self.last_name_label.pack()

        self.last_name_entry = Entry(master=None)
        self.last_name_entry.pack()

        self.contact_number_label = Label(master=None, text="Phone Number:")
        self.contact_number_label.pack()

        self.contact_number_entry = Entry(master=None)
        self.contact_number_entry.pack()


my_gui = MyFirstGUI(root)
root.mainloop()
