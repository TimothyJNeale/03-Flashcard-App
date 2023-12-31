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
    global num_1
    global num_2
    num_1 = IntVar()
    num_2 = IntVar()

    num_1.set(randint(0, 10))
    num_2.set(randint(0, 10))

    # Put random numbers on screen
    global add_label
    add_label = Label(add_frame, text=f"{num_1.get()} + {num_2.get()}", font=("helvetica", 32))
    add_label.pack(pady=20, padx=50)

    # Create answer box
    global add_answer
    add_answer = Entry(add_frame, font=("helvetica", 18))
    add_answer.pack(pady=10, padx=50)

    # Create submit button
    add_button = Button(add_frame, text="Answer", command=lambda: add_answer_func(num_1.get(), num_2.get(), add_answer.get()))
    add_button.pack(pady=10)

    global answer_label
    answer_label = Label(add_frame, text="Enter the correct value above", font=("helvetica", 18))
    answer_label.pack(pady=10)

# Create function to check add answer
def add_answer_func(num1, num2, answer):
    # Calculate the answer
    correct_answer = num1 + num2

    # Check if answer is correct
    if correct_answer == int(answer):
        answer_label.config(text="Correct Answer! " + str(num1) + " + " + str(num2) + " = " + str(correct_answer))
    else:
        answer_label.config(text="Incorrect Answer! " + str(num1) + " + " + str(num2) + " = " + str(correct_answer) + " not " + str(answer))

    # Clear the answer box
    add_answer.delete(0, "end")

    # Generate two new random numbers
    num_1.set(randint(0, 10))
    num_2.set(randint(0, 10))
    add_label.config(text=f"{num_1.get()} + {num_2.get()}")

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
    div_frame.pack(fill="both", expand=1)

    # Create two random numbers
    global num_1
    global num_2
    num_1 = IntVar()
    num_2 = IntVar()

    num_1.set(randint(0, 10))
    num_2.set(randint(1, 10))

    # Put random numbers on screen
    global div_label
    div_label = Label(div_frame, text=f"{num_1.get()} / {num_2.get()}", font=("helvetica", 32))
    div_label.pack(pady=20, padx=50)

    # Create answer box
    global div_answer
    div_answer = Entry(div_frame, font=("helvetica", 18))
    div_answer.pack(pady=10, padx=50)

    # Create submit button
    div_button = Button(div_frame, text="Answer", command=lambda: div_answer_func(num_1.get(), num_2.get(), div_answer.get()))
    div_button.pack(pady=10)

    global answer_label
    answer_label = Label(div_frame, text="Enter the correct value above", font=("helvetica", 18))
    answer_label.pack(pady=10)

# Create function to check add answer
def div_answer_func(num1, num2, answer):
    # Calculate the answer
    correct_answer = num1 / num2

    # Check if answer is correct
    if correct_answer == float(answer):
        answer_label.config(text="Correct Answer! " + str(num1) + " / " + str(num2) + " = " + str(correct_answer))
    else:
        answer_label.config(text="Incorrect Answer! " + str(num1) + " / " + str(num2) + " = " + str(correct_answer) + " not " + str(answer))

    # Clear the answer box
    div_answer.delete(0, "end")

    # Generate two new random numbers
    num_1.set(randint(0, 10))
    num_2.set(randint(1, 10))
    div_label.config(text=f"{num_1.get()} / {num_2.get()}")

# Hide menu frames
def hide_all_frames():
    # Loop thru and hide all frames
    for widget in start_frame.winfo_children():
        widget.pack_forget()
    for widget in add_frame.winfo_children():
        widget.pack_forget()
    for widget in subtract_frame.winfo_children():
        widget.pack_forget()
    for widget in multiply_frame.winfo_children():
        widget.pack_forget()
    for widget in div_frame.winfo_children():
        widget.pack_forget()

    # Hide all frames
    start_frame.pack_forget()
    add_frame.pack_forget()
    subtract_frame.pack_forget()
    multiply_frame.pack_forget()
    div_frame.pack_forget()

# Start screen
def home():
    # Hide all frames
    hide_all_frames()
    
    start_frame.pack(fill="both", expand=1)
    start_label = Label(start_frame, text="Welcome to Maths Flashcards", font=("helvetica", 18))
    start_label.pack(pady=20)

    a_button = Button(start_frame, text="Addition Flashcards", command=add).pack(pady=5)
    b_button = Button(start_frame, text="Subtraction Flashcards", command=subtract).pack(pady=5)
    c_button = Button(start_frame, text="Multiplication Flashcards", command=multiply).pack(pady=5)
    d_button = Button(start_frame, text="Division Flashcards", command=divide).pack(pady=5)

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
math_menu.add_command(label="Home", command=home)
math_menu.add_separator()
math_menu.add_command(label="Exit", command=root.quit)

# Create Math Frames    
add_frame = Frame(root, width=500, height=500)
subtract_frame = Frame(root, width=500, height=500, bg="red")
multiply_frame = Frame(root, width=500, height=500, bg="green")
div_frame = Frame(root, width=500, height=500)

# Show start screen
start_frame = Frame(root, width=500, height=500)    
home()

root.mainloop()