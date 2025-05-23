from tkinter import *

#Main 
window = Tk()
window.title("Password Generator App")
window['background']='dark sea green'
window.geometry("450x200") 

#Title Label
Label(window, text="Password Generator App", font="Arial 14 bold", bg="dark sea green").grid(row=0, columnspan=3, sticky=W)

#Entry to display generated password
Entry(window).grid(row=1, pady=3, sticky=W)

#Password length label 
Label(window, text="Password Length", font="Arial 12", bg="dark sea green").grid(row=2, column=0, sticky=W, pady=3, ipadx=3)

#Password length textbox
Entry(window, width=3).grid(row=2, column=1)

#Password strength radiobutton label
Label(window, text="Password Strength:", font="Arial 12", bg="dark sea green").grid(row=3, column=0, sticky=W, pady=3, ipadx=3)

#Three radiobuttons 
Radiobutton(window, text="Low", value=1, font="Arial 12", bg="dark sea green", highlightthickness=0).grid(row=3, column=1, ipadx=3, pady=3)

Radiobutton(window, text="Medium", value=2, font="Arial 12", bg="dark sea green", highlightthickness=0).grid(row=3, column=2, ipadx=3, pady=3)

Radiobutton(window, text="High", value=3, font="Arial 12", bg="dark sea green", highlightthickness=0).grid(row=3, column=3, ipadx=3, pady=3)

#Button that calls generate function
Button(window, text="Generate Password", font="Arial 12", bg = "sea green").grid(row=5, column=0, columnspan=5, pady=7, sticky=W)

window.mainloop()