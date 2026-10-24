import tkinter as tk
# import tkinter.font as tfont

window = tk.Tk()
window.title("Bittu's 1st Application")

# label = tk.Label(text = "Hello World!\t\t\t\t\t\t\t\n\n\n\n\n\n\n Have a nice Day\t\t\t\t\t\t\t\t\t\t ")
window.minsize(height = 700,width= 400)

# coustm_font = tfont.Font(slant = 'italic',family = "Times New Roman", weight  = 'bold', size = 15)
label = tk.Label(text = "Hello World..\n\n\n\n\n Have a nice Day !")





# label.pack(side = 'right') #bottom
label.pack(expand = True) #bottom
label.config(font = ("Courier New",25,'underline'))
window.mainloop()