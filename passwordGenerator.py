from tkinter import *
import random

# function to generate password
def generate():
	low = "abcdefghijklmnopqrstuvwxyz"
	medium = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
	high =  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_-+/?"

	strength = radio.get()
	length = lengthText.get()
	password = ""

	if strength == 1:
		for x in range(length):
			password += random.choice(low)

	if strength == 2:
		for x in range(length):
			password += random.choice(medium)

	if strength == 3:
		for x in range(length):
			password += random.choice(high)

	finishedPW.set(password)

#Main 
window = Tk()
window.title("Password Generator App")
window['background']='dark sea green'
window.geometry("450x200") 

# Configuring the grid layout
for i in range(4):
	window.grid_columnconfigure(i, weight=1)
for i in range(6):
	window.grid_rowconfigure(i, weight=1)

# Declare the control variables
finishedPW = StringVar()
lengthText = IntVar()
radio = IntVar()

#Title Label
Label(window, text="Password Generator App", font="Monoscape 14 bold", bg="dark sea green").grid(row=0, columnspan=3, sticky=W)

#Entry to display generated password
Entry(window, textvariable=finishedPW).grid(row=1, pady=3, sticky=W)

#Password length label 
Label(window, text="Password Length", font="Monoscape 12", bg="dark sea green").grid(row=2, column=0, sticky=W, pady=3, ipadx=3)

#Password length textbox
Entry(window, textvariable=lengthText, width=3).grid(row=2, column=1)

#Password strength radiobutton label
Label(window, text="Password Strength:", font="Monoscape 12", bg="dark sea green").grid(row=3, column=0, sticky=W, pady=3, ipadx=3)

#Three radiobuttons 
Radiobutton(window, text="Low", variable=radio, value=1, font="Monoscape 12", bg="dark sea green", highlightthickness=0).grid(row=3, column=1, ipadx=3, pady=3)

Radiobutton(window, text="Medium", variable=radio, value=2, font="Monoscape 12", bg="dark sea green", highlightthickness=0).grid(row=3, column=2, ipadx=3, pady=3)

Radiobutton(window, text="High", variable=radio, value=3, font="Monoscape 12", bg="dark sea green", highlightthickness=0).grid(row=3, column=3, ipadx=3, pady=3)

#Button that calls generate function
Button(window, text="Generate Password", font="Monoscape 12", bg = "sea green", command=generate).grid(row=5, column=0, columnspan=5, pady=7, sticky=W)

window.mainloop()