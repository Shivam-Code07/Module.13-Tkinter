import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title("Bittu's App")
window.minsize(height=900,width=400)
label = ttk.Label(text = "Enter Your Text!!\n",padding = '15')
label.pack(pady = 20)
label.config(font = ('Times New Roman',20,'bold'))

def click_here():
    label["text"] = f"Enter Your Text!!\n{(user_input.get()).title()}"


user_input = ttk.Entry(width = 30)
user_input.insert(0,"Enter your text: \n")
user_input.pack(pady = 20)
user_input.focus()


click_button = ttk.Button(text = "\n\tClick Here..\t\n", command = click_here)
click_button.pack(pady = 20)


sep = ttk.Separator(orient = "horizontal")
sep.pack(fill = 'x')
def commant_button():
    text["state"]  = "normal"


text = tk.Text(height = 5,width = 30,bg="gray")
text.pack(side = "top",expand = False,pady = 20)
text.insert("1.0","Description: \n")
text["state"]  = "disable"

text_data = text.get("1.0","end")
print(text_data)

def text_data_print():
    text_data = text.get("1.0","end")
    print(text_data)

text_data = ttk.Button(text = "\n\t Print Text \t\n", command = text_data_print)
text_data.pack(pady = 20)

commant1_button = ttk.Button(text = "\n\t Enable Commant Button \t\n", command = commant_button)
commant1_button.pack(pady = 20)


check_option = tk.IntVar()
def check_option_task():
    print(check_option.get())
check_button = ttk.Checkbutton( text = "Agree with the terms & conditions? ", variable = check_option, command =check_option_task )
check_button.pack()


def enable_button_fun():
    quit_button["state"]  = "enable"

enable_button = ttk.Button(text = "\n\t Enable Button \t\n", command = enable_button_fun)
enable_button.pack(pady = 20)


quit_button = ttk.Button(text = "\nQuit !\n", command = window.destroy)
quit_button.pack(pady = 20)
quit_button["state"]  = "disable"



window.mainloop() 