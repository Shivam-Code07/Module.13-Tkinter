import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("Bittu's App")
window.minsize(height=700,width=300)
label = ttk.Label(text = "\n\n\n\n\n\n\nEnter Your Text!!\n.......")
label.pack()
label.config(font = ('Times New Roman',20,'bold'))
def click_here():
    # if user_input == "":
    #     label["text"] = "Please enter the text: "
    # elif user_input == " ":
    #     label["text"] = "Please enter the text: " 
    # else:

    label["text"] = f"\n\n\n\n\n\n\nEnter Your Text!!\n{(user_input.get()).title()}"

# taking user input using entry class
user_input = ttk.Entry(width = 20)
user_input.pack()


click_button = ttk.Button(text = "\n\tClick Here...\t\n", command = click_here)
quit_button = ttk.Button(text = "\nQuit !\n", command = window.destroy)

click_button.pack()
quit_button.pack()

window.mainloop()