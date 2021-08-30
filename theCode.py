#import The tkinter package - Python interface
#import socket — Low-level networking interface for grep/Get the DNS/Host IP Adress
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import socket

# Creat screen Window, window size, title, bg(background-color)
screen = tk.Tk()
screen.geometry('700x270')
screen.title('DNS-IP')
screen["bg"] = "#c1c1c1"

# get Ip function
def getIP():
    #if + else statment,  check validation
    if("www." in hostname.get() and len(hostname.get()) != 0):
        try:
            ip = socket.gethostbyname(hostname.get())
            txtBox.delete(0, END)
            txtBox.insert(0, ip)
        except:
            messagebox.showerror("Error", "Enter Invalid Link! url starting with 'www' An example ===> www.google.com")
    else:
        messagebox.showerror("Error", "Enter Invalid Link! url starting with 'www' An example ===> www.google.com")


# Buttons hover style functions on_enter - on_leave
def on_enter(e):
    btn['bg'] = 'gray30'


def on_leave(e):
    btn['bg'] = 'gray73'


def on_enter2(e):
    exit_Button['bg'] = 'gray30'


def on_leave2(e):
    exit_Button['bg'] = 'gray73'

#Entry + label "Enter DNS/Target"
myLabel = Label(screen, text="Enter DNS/Target IP:", font=('Arial', 12, 'bold'), bg = "#c1c1c1")
myLabel.place(x=50, y=60)
hostname = Entry(screen, width=36, bd=4)
hostname.place(x=230, y=60)

# Button Get IP
btn = tk.Button(screen, text="Get IP", pady=5, bd=2, width=15, font=('Arial', 12, 'bold'),  bg='gray73',
                activebackground="white", command=getIP)
btn.place(x=260, y=100)
btn.bind("<Enter>", on_enter)
btn.bind("<Leave>", on_leave)

# Entry + label Target IP(Result Entry)
myLabel = Label(screen, text="Target IP Is:", font=('Arial', 12, 'bold'), bg = "#c1c1c1")
myLabel.place(x=120, y=160)
txtBox = Entry(screen, width=36, bd=4)
txtBox.place(x=230, y=160)

# Exit Button
exit_Button = tk.Button(screen, text="EXIT", width=12, height=1, bd=10, font=("Arial", 12, "bold"), bg='gray73',
                        activebackground="red", command=screen.destroy)
exit_Button.place(x=530, y=200)
exit_Button.bind("<Enter>", on_enter2)
exit_Button.bind("<Leave>", on_leave2)

screen.mainloop()