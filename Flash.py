from tkinter import *
from random import randint

root = Tk()
root.title("Maths Flashcards")
root.geometry("500x500")
root.iconbitmap("01 Nenebiker.ico")

# Create function to add two numbers
def add():
    hide_all_frames()
    add_frame.pack(fill="both", expand=1)

    # Create two random numbers
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)

    # Put random numbers on screen
    add_label = Label(add_frame, text=f"{num_1} + {num_2}", font=("helvetica", 32))
    add_label.pack(pady=20, padx=50)

    # Create answer box
    add_answer = Entry(add_frame, font=("helvetica", 18))
    add_answer.pack(pady=10, padx=50)

    # Create submit button
    add_button = Button(add_frame, text="Answer", command="")
    add_button.pack(pady=10)


# Create function to subtract two numbers
def subtract():
    hide_all_frames()
    subtract_frame.pack(fill="both", expand=1)

# Create function to multiply two numbers
def multiply():
    hide_all_frames()
    multiply_frame.pack(fill="both", expand=1)

# Create function to divide two numbers
def divide():
    hide_all_frames()
    divide_frame.pack(fill="both", expand=1)  

# Hide menu frames
def hide_all_frames():
    # Loop thru and hide all frames
    for widget in add_frame.winfo_children():
        widget.pack_forget()
    for widget in subtract_frame.winfo_children():
        widget.pack_forget()
    for widget in multiply_frame.winfo_children():
        widget.pack_forget()
    for widget in divide_frame.winfo_children():
        widget.pack_forget()

    # Hide all frames
    add_frame.pack_forget()
    subtract_frame.pack_forget()
    multiply_frame.pack_forget()
    divide_frame.pack_forget()

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

# Create Math Frames
add_frame = Frame(root, width=500, height=500)
subtract_frame = Frame(root, width=500, height=500, bg="red")
multiply_frame = Frame(root, width=500, height=500, bg="green")
divide_frame = Frame(root, width=500, height=500, bg="yellow")




root.mainloop()