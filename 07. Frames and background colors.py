import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("Tiranga")
window.minsize(height=200,width=400)
my_frame =ttk.Frame() 
my_frame.pack(side = "top",expand = True, fill = 'both')
# my_frame.pack(side = "left",expand = True, fill = 'both')

label1 = tk.Label(my_frame,text = "1st Box..",bg="red")
label1.pack(side = "top",expand = True, fill = 'both')
label2 = tk.Label(text = "2nd Box..",bg="white")
label2.pack(side = "top",expand = True, fill = 'both')
label3 = tk.Label(text = "3rd Box..",bg="green")
label3.pack(side = "top",expand = True, fill = 'both')

window.mainloop()