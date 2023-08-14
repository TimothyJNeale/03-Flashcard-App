from tkinter import *

root = Tk()
root.title("Maths Flashcards")
root.geometry("500x500")
root.iconbitmap("01 Nenebiker.ico")

# Create function to add two numbers
def add():
    pass

# Create function to subtract two numbers
def subtract():
    pass

# Create function to multiply two numbers
def multiply():
    pass

# Create function to divide two numbers
def divide():
    pass


# Define main menu
main_menu = Menu(root)
root.config(menu=main_menu)

# Create meny items
math_menu = Menu(main_menu)
main_menu.add_cascade(label="Maths", menu=math_menu)
math_menu.add_command(label="Add", command=add)
math_menu.add_command(label="Subtract", command=subtract)
math_menu.add_command(label="Multiply", command=multiply)
math_menu.add_command(label="Divide", command=divide)
math_menu.add_separator()
math_menu.add_command(label="Exit", command=root.quit)



root.mainloop()