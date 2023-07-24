#importing required libraries for TechVidvan Password Generator project using Python

#from msilib.schema import CheckBox

import random
from tkinter import *
import string
import pyperclip #this module is used to copy and paste inside and you can outside as well
import tkinter #creating a main
def password_generate(leng):
     valid_char='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_'#characters of the password
     password=''.join(random.sample(valid_char,leng))#random generation of password
     pyperclip.copy(password)#copy the text which is genretated and you can paste anywhere where
     l.config(text= password)#displaying password
     l.place(x=150,y=50)
     



main = Tk()
main.title('Passwd_gen')#main title
main.geometry('500x500')#main geometry

Label(main,font=('Chiller',20),text='PASSWORD GENERATOR').pack()#giving label to main
#creating a main
#function to generate password
#converting string input to integer
l =Label(main, text = "", font=('bold', 20))#displaying password
l.place(x=190,y=50)
len1=tkinter.IntVar()
len2=tkinter.IntVar()
len3=tkinter.IntVar()
len4=tkinter.IntVar()
Checkbutton(main,text='4 character',onvalue=4, offvalue=0,variable=len1).place(x=200,y=120)#creating checkbox
Checkbutton(main,text='6 character',onvalue=6, offvalue=0,variable=len2).place(x=200,y=140)#creating checkbox
Checkbutton(main,text='8 character',onvalue=8, offvalue=0,variable=len3).place(x=200,y=160)#creating checkbox
Checkbutton(main,text='16 character',onvalue=16, offvalue=0,variable=len4).place(x=200,y=180)#creating checkbox


#function to check the checkbox

def get_len():
    
      if len1.get() == 4:
         password_generate(4)
      elif len2.get() == 6:
         password_generate(6)
      elif len3.get() == 8:
         password_generate(8)
      elif len4.get() == 16:
         password_generate(16)
      else:
         password_generate(6)

Button(main,text='Generate',font=('normal',10), bg='green',command=get_len).place(x=200,y=240)
main.mainloop()#run the main
