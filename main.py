'''this is my first hackathon and hackathon project please support'''
'''This is the Gui based password generator.'''
from tkinter import *
import random
import string
import datetime

root =Tk()
root.config(bg="#e61a8a")
root.title("Generate your own password...")
root.geometry('2000x1000')
root.maxsize(2000, 1000)
root.minsize(2000, 1000)
txt = Label(root,bg="#e61a8a", text="Welcome to the world best password generator!\n", font=("valera round", 30), foreground="#0450f3")
txt.pack()


d = datetime.datetime.now()
#giving them value that which type of variable they are
ent1_value = StringVar()
ent_value = StringVar()
ent2_value = StringVar()
ent3_value = IntVar()

# var1 = ent1_value.get()
# var2 = ent_value.get()
# var3 = ent2_value.get()
# var_4 = ent3_value.get()

def password():
    paswa = ''.join(random.choices(string.ascii_uppercase+string.digits+string.ascii_lowercase, k=ent3_value.get()))
    return paswa

def get_value():
    print(f"{ent1_value.get(), ent_value.get(), ent2_value.get(), ent3_value.get()}")
    b = f"\nDate&Time - {d},\nName is {ent1_value.get()},\nThe company or website name is {ent_value.get()},\nThe email address is {ent2_value.get()},\nThe password is {password()}"
    with open("password.txt", "a") as f:
        f.write(b)
    password()
    
    text = Label(root,bg="#e61a8a", text="Your password has been generated.\nIt is stored in password.txt file with all the information.\nThankyou for giving us you so much precious time.\nHave fantastic time.", font=("valera round", 20), foreground="#20f304").place(x=240, y=440)
    # text.tag_config(background="antiquewhite", foreground="white")

# name
txt1 = Label(root,bg="#e61a8a", text="What is your name?: ", font=("valera round", 17, "bold")).place(x=500 ,y=115)
ent1 =Entry(root, textvariable=ent1_value).place(x=975 ,y=127)

#company name
txt2 = Label(root, bg="#e61a8a",text="Enter the company/site name for which you want to make the password:", font=("valera round", 15, "bold")).place(x=50, y=180)
ent = Entry(root, textvariable=ent_value, width=25).place(x= 1525, y=189)

#email
txt3=Label(root, bg="#e61a8a",text="Enter the email of your account of which you want to make password of:   ", font=("valera round", 15, "bold")).place(x=50, y=250)
ent2=Entry(root, textvariable=ent2_value, width=25).place(x=1525, y=260)

#length
txt1=Label(root, bg="#e61a8a",text="Enter of which length of your password should be(please enter only digit):", font=("valera round", 15, "bold")).place(x=50, y=320)
ent3 = Entry(root, textvariable=ent3_value, width=25).place(x=1525, y=330)

#button
button = Button(root,bg="antiquewhite", text='Submit', width=7, command=get_value).place(x=800, y=390)

root.mainloop()
