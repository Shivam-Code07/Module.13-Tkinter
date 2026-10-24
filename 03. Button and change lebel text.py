import tkinter as tk

window = tk.Tk()
window.title("My Application")
window.minsize(height = 600,width = 350)


label = tk.Label(text = "This Message is Real") 
label.pack()
label.config(font = ("Times New Roman",15,'bold'))

# Changed message
# label["text"] = "Changed message !!"

number_of_clic = 0
def click_here():
    global number_of_clic

    if number_of_clic == 0:
        label["text"] = "\n\nChanged message !!"
    elif number_of_clic == 1:   
        label["text"] = "\n\nThis Message Changed 2nd Times !!"
    elif number_of_clic == 2:   
        label["text"]= "\n\nThis Message Changed 3rd Times !!"    
    else: 
        label["text"] = f"\n\nThis Message Changed {1 + number_of_clic}th Times !!"
    number_of_clic += 1


#Button
button = tk.Button(text =  "Click Here !", command = click_here)
button.pack()
window.mainloop()