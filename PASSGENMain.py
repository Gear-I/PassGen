import random
from tkinter import *
from tkinter import messagebox
import pyperclip

# Define window
def disable_event():
    pass
app = Tk()
app.geometry("650x200")
app.title("Welcome to Password Generator Version 1.0, Licensed under GPLv3 - Dielle De Noon")
app.iconbitmap('PassGen4.ico')
app.protocol("WM_DELETE_WINDOW", disable_event)
# Items used to generate password
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
special = "!@#$%^&*()"
Symbols = ":;<,>.?/|\+_-[{]}"
unicode = "\u0394\u03A9\u03C0\u03F4"
# From which items you want to generate password
upper = BooleanVar()
lower = BooleanVar()
nums = BooleanVar()
spec = BooleanVar()
sym = BooleanVar()
uni = BooleanVar()

everything = ""

def check_1():
    global upper
    global everything
    # Add items what you want to everything variable
    if upper.get() == True:
        everything += uppercase_letters
    if upper.get() == False:
        everything.replace("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "")
def check_2():
    global  lower
    global everything
    if lower.get() == True:
        everything += lowercase_letters
    if lower.get() == False:
        everything.replace("abcdefghijklmnopqrstuvwxyz", "")
def check_3():
    global nums
    global everything
    if nums.get() == True:
        everything += digits
    if nums.get() == False:
        everything.replace("0123456789", "")
        
def check_4():
    global spec
    global everything
    if spec.get() == True:
        everything += special
    if spec.get() == False:
        everything.replace("!@#$%^&*()", "")
def check_5():
    global sym
    global everything
    if sym.get() == True:
        everything += Symbols
    if sym.get() == False:
        everything.replace(":;<,>.?/|\+_-[{]}", "")
def check_6():
    global uni
    global everything
    if uni.get() == True:
        everything += unicode
    if uni.get() == False:
        everything.replace("\u0394\u03A9\u03C0\u03F4", "")



CheckboxLabel_1 = Label(app, text="UpperCase Letters")
CheckboxLabel_1.grid(row=2, column=5)

CheckboxLabel_2 = Label(app, text="LowerCase Letters")
CheckboxLabel_2.grid(row=3, column=5)

CheckboxLabel_3 = Label(app, text="Numbers")
CheckboxLabel_3.grid(row=4, column=5)

CheckboxLabel_4 = Label(app, text= "Special Characters")
CheckboxLabel_4.grid(row=5, column=5)

CheckboxLabel_5 = Label(app, text="Symbols")
CheckboxLabel_5.grid(row=6, column=5)

CheckboxLabel_6 = Label(app, text= "Unicodes")
CheckboxLabel_6.grid(row=7, column=5)

Checkbox_1 = Checkbutton(app, text="", variable=upper, onvalue = True, offvalue= False, command=check_1)
Checkbox_1.grid(row=2, column=6)

Checkbox_2 = Checkbutton(app, text="", variable=lower, onvalue = True, offvalue= False, command=check_2)
Checkbox_2.grid(row=3, column=6)

Checkbox_3 = Checkbutton(app, text="", variable=nums, onvalue = True, offvalue= False, command=check_3)
Checkbox_3.grid(row=4, column=6)

Checkbox_4 = Checkbutton(app, text="", variable=spec, onvalue= True, offvalue= False, command=check_4)
Checkbox_4.grid(row=5, column=6)

Checkbox_5 = Checkbutton(app, text="", variable=sym, onvalue= True, offvalue= False, command=check_5)
Checkbox_5.grid(row=6, column=6)

Checkbox_6 = Checkbutton(app, text="", variable=uni, onvalue= True, offvalue= False, command=check_6)
Checkbox_6.grid(row=7, column=6)

LengthText = Label(app, text="Length: ")
LengthText.grid(row=0, column=5)

Space = Label(app, text="")
Space.grid(row=0, column=4)

length = Entry(app, width=4) # Length of your password
length.insert(0, "") # Default length 
length.grid(row=0, column=6)

AmountText = Label(app, text="Amount: ")
AmountText.grid(row=1, column=5)

amount = Entry(app, width=4) # Amount of generated passwords
amount.insert(0, "1") # Default amount
amount.grid(row=1, column=6)

Generated = Label(app, text="Generated password:") 
Generated.grid(row=0, column=1)

Space_1 = Label(app, text="")
Space_1.grid(row=1, column=0)

PasswordText = Entry(app, width=25) # Text box
PasswordText.grid(row=1, column=1)


# Generating password function
def generate_password():
    PasswordText.delete(0, END) # Clear text box before writing a new password
    for x in range(int(amount.get())):
        password = "".join (random.sample(everything, int(length.get())))
        PasswordText.insert(0, password) # Past password into text box
    Generated= Label(app, text="Password Generated.", fg="green") # Show info
    Generated.grid(row=3, column=1)
    Generated.after(10000, Generated.destroy)
if not upper.get() or lower.get() or nums.get() or spec.get() or sym.get() or uni.get():
    messagebox.showwarning(title="Warning", message="Enter Number of characters (Max Characters is 50) in the length box select three or more options to generate password")

def reset():
    PasswordText.delete(0, END)
    Checkbox_1.deselect()
    Checkbox_2.deselect()
    Checkbox_3.deselect()
    Checkbox_4.deselect()
    Checkbox_5.deselect()
    Checkbox_6.deselect()
    length.delete(0, END)
    
    


Submit = Button(app, text="Generate", command=lambda:[generate_password(), save_password()] ) # Generating button
Submit.grid(row=2, column=1)
Reset = Button(app, text="Reset", command=reset)  # Reseting PassGen Button
Reset.grid(row=4, column=1)
# Copying password to clipboard
def copytoclipboard():
    pyperclip.copy(PasswordText.get())
    messagebox.showinfo(title="Info", message="Password copied to clipboard.")
    PasswordText.delete(0, END)

# Saving Password

def Check():
    if YES == True:
        messagebox.showwarning(title= "Warning", message= "This function is in progress")
        exit()
    if NO == True:
        messagebox.showinfo(title= "Confirmation Message", message= "Thank you for your response")
        exit()


def save_password():
    Win = Toplevel
    Win = Tk()
    Win.geometry("650x200")
    Win.title("Save Password Confirmation")
    Win.iconbitmap('PassGen4.ico')
    SP=Label(Win, text="Would you like to save the generated password? Please check 'Yes' or 'No' ")
    SP.pack(pady=10)
    YES= Button(Win, text="Yes", variable= YES, onvalue= True, offvalue= False, command=Check)
    YES.pack(pady=15)
    NO = Button(Win, text="No", variable= NO, onvalue=True, offvalue=False, command=Check)
    NO.pack(pady=20)
    



def close_app():
    app.destroy()
Copy = Button(app, text="Copy", command=copytoclipboard) # Copying button
Copy.grid(row=1, column=3)
Exit= Button(app,text= "Exit", command=close_app)
Exit.grid(row=6, column=1)

app.mainloop()









