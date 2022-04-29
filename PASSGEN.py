from tkinter import *
import db
import string, random

#import Author as Dielle De Noon
#v1.0
#import the neccesary modules: 

#input the length of password
length = int(input('\nHow Many Character: '))

#define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
#string.ascii_letters

#combine the data
all = lower + upper + num + symbols

#use random
temp = random.sample(all, length)

#create the password
password = "".join(temp)

#print the password
print(password)








