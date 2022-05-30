from tkinter import *
import tkinter
import random
main_screen = Tk()
import db
def create_unique_password ():
     # Set variable for open file name
    global open_status_name
    open_status_name = True

    global selected
    selected = True  

#import Author as Dielle De Noon
#v1.0

def database():
            conn = db.db_create_database()
            db.db_create_table(conn)
            pwd = create_unique_password(var)
            db.insert(conn, APPLICATION_NAME=applicationName.get(), EMAIL_ID=emailId.get(), PASSWORD=pwd)
            return pwd


def generate_pwd():
    screen_2 =Toplevel(main_screen)
    screen_2.title("Give inputs")
    screen_2.geometry("200x200")
    #pwd = StringVar()
    pwd =database()
    Label(screen_2, text="Your Password is: ").pack()
    Label(screen_2, text=pwd, bg="white", font=('Times New Roman', 14)).pack()
    applicationEntry.delete(0, END)
    emailIdEntrty.delete(0, END)

def main():
    global main_screen
    global applicationName, emailId, applicationEntry, emailIdEntry
main_screen = Tk()
main_screen.geometry("500x500")
main_screen.title("Welcome to Password Generator Version 1.0")
var =IntVar()
##Label Frame
lf = LabelFrame(main_screen, text="How Many Characters")
lf.pack(pady=20)
    # Create Entry Box to Designate Number of Character
my_entry = Entry(lf, font=("Times New Roman", 18))
my_entry.pack(pady=20, padx=20)
Label(text="").pack()
applicationName = StringVar()
emailId = StringVar()
Label(main_screen, text="Application Name: ", font=("Times New Roman", 20)).pack()
applicationEntry = Entry(main_screen, textvariable=applicationName)
applicationEntry.pack()
Label(main_screen, text="Email ID: ", font=("Times New Roman", 20)).pack()
emailIdEntry = Entry(main_screen, textvariable=emailId)
emailIdEntry.pack()
Label(text="").pack()
# condition variables
cond1 = IntVar()
cond2 = IntVar()
cond3 = IntVar()
cond4 = IntVar()
length = IntVar()

# charecter lists
list_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
list_2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']
list_3 = ['!', '@', '#', '$', '%', '^', '&', '*']
list_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# function to generate password
def password():
    final_list = []
    ln = length.get()
    if (cond3.get()):
        final_list.append(list_1)
    if (cond4.get()):
        final_list.append(list_2)
    if (cond2.get()):
        final_list.append(list_3)
    if (cond1.get()):
        final_list.append(list_4)
    bound = cond1.get() + cond2.get() + cond3.get() + cond4.get()
    if not (bound):
        return ("Nothing selected")
    password = []
    for i in range(ln):
        if (i == 0):
            a = 1
        else:
            a = random.randint(1, bound)
        k = final_list[a - 1]
        b = random.randint(0, len(k) - 1)
        password.append(str(k[b]))
    return (''.join(password))

# gloabal password variable
pswrd = StringVar()
pswrd.set(password())
txt_1 = tkinter.Label(main_screen, textvariable=pswrd, font=("Times New Roman", 20))

# function to display generated password
def display_password():
    global txt_1
    txt_1.pack_forget()
    pswrd.set(password())
    txt_1 = tkinter.Label(main_screen, textvariable=pswrd, font=("Times New Roman", 20))
    txt_1.pack()

#top labels
label_1 = tkinter.Label(main_screen, text="Select two options or more\n", font=("Times New Roman", 20))
label_1.pack()

# creating gui components
chkbutton_1 = tkinter.Checkbutton(main_screen, text='Numbers', variable=cond1, onvalue=1, offvalue=0)
chkbutton_2 = tkinter.Checkbutton(main_screen, text='Special Charecters', variable=cond2, onvalue=1, offvalue=0)
chkbutton_3 = tkinter.Checkbutton(main_screen, text='Small Letters', variable=cond3, onvalue=1, offvalue=0)
chkbutton_4 = tkinter.Checkbutton(main_screen, text='Capital Letters', variable=cond4, onvalue=1, offvalue=0)
button_1 = tkinter.Button(main_screen, text="Generate password", command=display_password)
# run created components
chkbutton_1.pack()
chkbutton_2.pack()
chkbutton_3.pack()
chkbutton_4.pack()
my_entry.pack()
applicationEntry.pack()
emailIdEntry.pack()
button_1.pack()

main_screen.mainloop()








