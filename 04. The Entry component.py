import tkinter as tk
window = tk.Tk()
window.title("Bittu's App")
window.minsize(height=700,width=300)
label = tk.Label(text = "Hiii !!\nEnter Your Text..")
label.pack()
label.config(font = ('Times New Roman',20,'bold'))
counter = 1
def click_here():
    global counter
    # label["text"] = f"You click {counter} times."
    label["text"] = (user_input.get()).title()
    counter +=1

# taking user input using entry class
# user_input = Entry(text = "Enter anything...")
user_input = tk.Entry(width = 20)
user_input.pack()


button = tk.Button(text = "Click Here...", command = click_here)
button.pack()
window.mainloop()
