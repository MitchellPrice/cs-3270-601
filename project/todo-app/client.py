from tkinter import Tk

#from db import TodoDatabase
from rest import TodoClient
from ui import TodoListUI

def main():
#     todo_db = TodoDatabase()
    todo_client = TodoClient()
    root = Tk()
    todo_ui = TodoListUI(root, todo_client)
    root.wm_geometry('400x600')
    root.mainloop()


if __name__ == "__main__":
    main()

