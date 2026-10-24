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
text.pack(side = "left",expand = False,pady = 20)
text.insert("1.0","Description: \n")
text["state"]  = "disable"

text_data = text.get("1.0","end")
print(text_data)

def text_data_print():
    text_data = text.get("1.0","end")
    print(text_data)

text_data = ttk.Button(text = "\n\t Print Text \t\n", command = text_data_print)
text_data.pack(side = "left",expand = False,pady = 20)

commant1_button = ttk.Button(text = "\n\t Enable Commant Button \t\n", command = commant_button)
commant1_button.pack(pady = 20)


check_option = tk.IntVar()
def check_option_task():
    print(check_option.get())
check_button = ttk.Checkbutton( text = "Agree with the terms & conditions? ", variable = check_option, command =check_option_task )
check_button.pack(side = "left",expand = False,pady = 20)


def enable_button_fun():
    quit_button["state"]  = "enable"

enable_button = ttk.Button(text = "\n\t Enable Button \t\n", command = enable_button_fun)
enable_button.pack(pady = 20)


quit_button = ttk.Button(text = "\nQuit !\n", command = window.destroy)
quit_button.pack(pady = 20,side = "bottom",expand = True)
quit_button["state"]  = "disable"
radio_value = tk.StringVar()


def get_radio_value():
    print(radio_value.get())

button_1 = ttk.Radiobutton(text = "Male", variable = radio_value,value = "Male" , command = get_radio_value)
button_2 = ttk.Radiobutton(text = "Female", variable = radio_value,value = "Female",command = get_radio_value)
button_1.pack(side = "left",expand = False,pady = 20)
button_2.pack(side = "left",expand = False,pady = 20)

selected_country = tk.StringVar()
country = ttk.Combobox(value = ("India","Nepal","Bangladesh","Pakistan","China","Sri lanka"),textvariable = selected_country)
country["state"] = "readonly"
country.pack()

# def display_country(event):
#     print(f"Selected Country is {selected_country.get()}") # jo baad mai bind hoga wahi sirf work karega pehle vala kaam karna band kr dega !
# country.bind("<<ComboboxSelected>>", display_country)

country_label = ttk.Label(text = "please select your Country !", padding = '15')
country_label.pack(pady = 20)
country_label.config(font = ('Times New Roman',20,'bold'))

def label_country(event):
    country_label["text"] = f"Selected Country is {selected_country.get()}"
country.bind("<<ComboboxSelected>>", label_country)


#Listbox()
food_items = ("Salad", "Garlic Bread", "Burgar", "Pizza", "Veg-Chomin")
fav_food = tk.StringVar(value = food_items)
food_list = tk.Listbox(listvariable = fav_food,bg = "gray",height = 5, selectmode= "extended")
food_list.pack()

def display_fav_food(event):
    food_indices = food_list.curselection()
    for i in food_indices:
        print(food_list.get(i))
food_list.bind("<<ListboxSelect>>",display_fav_food)


window.mainloop() 