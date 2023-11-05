"""
Написать GUI приложение, которое представляет собой
упрощенный файловый менеджер, с возможностью создания,
удаления и переименования директорий и файлов.
"""

from tkinter import *
import os


class FileManager(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("File Manager")
        self.pack(fill=BOTH, expand=1)

        def create_folder():
            try:
                folder_name = self.entry_path.get()
                os.mkdir(folder_name)
                self.entry_path.delete(0, END)
                self.listBox.insert(END, folder_name)
            except:
                print("Error")

        def delete_item():
            try:
                selected_item = self.listBox.curselection()
                item = self.listBox.get(selected_item)
                print("Delete: " + item)
                if os.path.isdir(item):
                    os.rmdir(item)
                else:
                    os.remove(item)
                self.listBox.delete(selected_item)
            except:
                print("Error")

        def rename_item():
            try:
                new_name = self.entry_name.get()
                selected_item = self.listBox.curselection()
                item = self.listBox.get(selected_item)
                print("Rename: " + item)
                os.rename(item, new_name)
                self.listBox.delete(selected_item)
                self.listBox.insert(END, new_name)
            except:
                print("Error")



        self.label_path = Label(self, text="Path:")
        self.label_path.grid(row=0, column=0)
        self.entry_path = Entry(self)
        self.entry_path.grid(row=0, column=1)
        self.btn_create_folder = Button(self, text="Create Folder", command=create_folder, fg="white", bg="blue")
        self.btn_create_folder.grid(row=0, column=2)

        self.btn_delete = Button(self, text="Delete", command=delete_item, fg="white", bg="red")
        self.btn_delete.grid(row=2, column=0)

        self.btn_rename = Button(self, text="Rename", command=rename_item, fg="white", bg="green")
        self.btn_rename.grid(row=2, column=1)
        self.entry_name = Entry(self)
        self.entry_name.grid(row=2, column=2)

        self.listBox = Listbox(self)
        self.listBox.grid(row=1, column=0, columnspan=3)

        files = os.listdir(".")
        for file in files:
            self.listBox.insert(END, file)

root = Tk()
app = FileManager(root)
root.mainloop()