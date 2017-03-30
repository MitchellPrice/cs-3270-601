from tkinter import Tk

from db import TodoDatabase
from ui import TodoListUI

def main():
    todo_db = TodoDatabase()
    root = Tk()
    todo_ui = TodoListUI(root, todo_db)
    root.wm_geometry('400x600')
    root.mainloop()


if __name__ == "__main__":
    main()

