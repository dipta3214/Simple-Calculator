from tkinter import *

root = Tk()

#Functions for numbers
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
	e.delete(0, END)

def button_add():
 	first_number = e.get()
 	global f_num
 	global math
 	math = "add"
 	f_num = int(first_number)
 	e.delete(0, END)

def button_subtraction():
 	first_number = e.get()
 	global f_num
 	global math
 	math = "subtraction"
 	f_num = int(first_number)
 	e.delete(0, END)

def button_multiplication():
 	first_number = e.get()
 	global f_num
 	global math
 	math = "multiplication"
 	f_num = int(first_number)
 	e.delete(0, END)

def button_division():
 	first_number = e.get()
 	global f_num
 	global math
 	math = "division"
 	f_num = int(first_number)
 	e.delete(0, END)

def button_equal():
	second_number = e.get()
	e.delete(0, END)

	if math == "add":
	   e.insert(0, f_num + int(second_number))

	if math == "subtraction":
		e.insert(0, f_num - int(second_number))

	if math == "multiplication":
		e.insert(0, f_num * int(second_number))

	if math == "division":
		e.insert(0, f_num / int(second_number))

#Enter
e = Entry(root, width=25, borderwidth=5)
e.grid(row=0, column=0, columnspan=3)

#Buttons
button_7 = Button(root, padx=20, text="7", command=lambda: button_click(7))
button_8 = Button(root, padx=20, text="8",  command=lambda: button_click(8))
button_9 = Button(root, padx=20, text="9" , command=lambda: button_click(9))
button_4 = Button(root, padx=20, text="4",  command=lambda: button_click(4))
button_5 = Button(root, padx=20, text="5",  command=lambda: button_click(5))
button_6 = Button(root, padx=20, text="6",  command=lambda: button_click(6))
button_1 = Button(root, padx=20, text="1",  command=lambda: button_click(1))
button_2 = Button(root, padx=20, text="2", command=lambda: button_click(2))
button_3 = Button(root, padx=20, text="3", command=lambda: button_click(3))
button_0 = Button(root, padx=48, text="0", command=lambda: button_click(0))
button_add = Button(root, padx=20, text="+", command=button_add)
button_subtraction = Button(root, padx=20, text="-", command=button_subtraction)
button_multiplication = Button(root, padx=20, text="*", command=button_multiplication)
button_division= Button(root, padx=20, text="/", command=button_division)
button_equal= Button(root, padx=20, pady=18, text="=", command=button_equal)
button_clear= Button(root, padx=20, text="C", command=button_clear)

#Buttons Displaying
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_0.grid(row=4,column=0, columnspan=2)
button_add.grid(row=5,column=0)
button_subtraction.grid(row=5,column=1)
button_multiplication.grid(row=6,column=0)
button_division.grid(row=6,column=1)
button_equal.grid(row=5, rowspan=2, column=2)
button_clear.grid(row=4, column=2)


root.mainloop()