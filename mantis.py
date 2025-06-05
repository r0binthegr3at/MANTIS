from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askfloat
from tkinter.simpledialog import askstring
from tkinter import ttk
import os, sys, time, urllib, re
from bs4 import BeautifulSoup


root = Tk()
root.title("MANTIS")
root.geometry("300x200")

#Functions defined
def email_info():
    tar_email = input("<Target Email>: ")

def who():
    WDOM = askstring("Enter domain>: ")
    HT = urllib.urlopen(WDOM)
    WD_H = HT.read()
    BS_Ob = BeautifulSoup()
    Ftxt = open("who.txt", 'a')
    who_is = BS_Ob.body.find('div', attrs={'class' : 'stats'})
    who_is1 = str(who_is)
    for m in re.finditer("Domain Name: ", who_is1):
        s = m.start()

    line_raw = who_is1[s:]
    lines =  lines_raw.split
    i = 0
    for line in lines:
        file_text.writelines(line)
        file_text.writelines("\n")
        print(line)
        i=i+1
        if i==17:
            break

    file_text.writelines("-"*50)
    file_text.writelines("\n")
    file_text.close()


#In here


#Main code
menubar = Menu(root)
email_menu = Menu(menubar, tearoff=0)
dom_menu = Menu(menubar, tearoff=0)
uname_menu = Menu(menubar, tearoff=0)
scrap_menu = Menu(menubar, tearoff=0)
exit_menu = Menu(menubar, tearoff=0)
#In here

