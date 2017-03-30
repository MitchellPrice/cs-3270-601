from tkinter import Menu, Label, Button, Frame, Checkbutton, Entry, END
from tkinter import messagebox, filedialog


class TodoListUI:
    def __init__(self, root, db):
        self.__root = root
        self.__db = db
        self.__setup_view()
        self.__setup_menu()
        self.__list_todos()

    def __setup_view(self):
        self.__header_label = Label(self.__root, text='Todo App')
        self.__header_label.pack()

        self.__todo_frame = Frame(self.__root)
        self.__todo_frame.pack()

        self.__new_todo_frame = Frame(self.__root)
        self.__new_todo_frame.pack()

        new_task_label = Label(self.__new_todo_frame, text='Todo')
        new_task_label.grid(row=0, column=0)
        self.__task_entry = Entry(self.__new_todo_frame)
        self.__task_entry.grid(row=0, column=1)

        new_task_button = Button(self.__new_todo_frame, text='Create', command=self.__create_todo)
        new_task_button.grid(row=1, column=1)

    def __setup_menu(self):
        self.__menubar = Menu(self.__root)

        filemenu = Menu(self.__menubar, tearoff=0)
        filemenu.add_command(label='Open', command=self.__open_db)
        filemenu.add_command(label='Toggle Completed', command=self.__toggle_completed)
        filemenu.add_separator()
        filemenu.add_command(label='Quit', command=self.__root.quit)
        self.__menubar.add_cascade(menu=filemenu, label='File')

        aboutmenu = Menu(self.__menubar, tearoff=0)
        aboutmenu.add_command(label='About', command=self.__show_about)
        self.__menubar.add_cascade(menu=aboutmenu, label='About')

        self.__root.config(menu=self.__menubar)

    def __open_db(self):
        selected_file = filedialog.askopenfilename()
        print(selected_file)

    def __toggle_completed(self):
        pass

    def __show_about(self):
        messagebox.showinfo('About', 'Created for CS 3270')

    def __create_todo(self):
        new_todo = self.__task_entry.get()
        self.__task_entry.delete(0, END)

        self.__db.insert_todo(new_todo)


    def __create_todo_check(self, todo_id):
        def inner():
            self.__db.update_completed(todo_id)
        return inner

    def __list_todos(self):
        todos = self.__db.list_todos()

        for i,t in zip(range(len(todos)), todos):
            task_box = Checkbutton(self.__todo_frame,
                                   text='',
                                   command=self.__create_todo_check(t[0]))
            task_box.grid(row=i, column=0)

            task_label = Label(self.__todo_frame, text=t[1])
            task_label.grid(row=i, column=1)









