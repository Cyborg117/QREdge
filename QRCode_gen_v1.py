import requests
import os
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msg
from tkinter import colorchooser
from tkinter import filedialog
from PIL import ImageTk,Image

def datahelp():
    global r3
    r3=Toplevel(root)
    r3.title("Data Help")
    r3.resizable(False,False)
    r3.iconbitmap("icon.ico")
    mf3=ttk.Frame(r3,padding='3 3 12 12')
    mf3.pack(fill="both",expand="yes")
    mf3.rowconfigure(0,weight=1)
    mf3.columnconfigure(0,weight=1)
    l=ttk.Label(mf3,background="blue")
    l.pack(fill="both",expand="yes")
    ttk.Label(l,text="The Following is the Format that can be used in Data",foreground="yellow",background="blue").grid(row=2,column=0,sticky="w")
    ttk.Label(l,text="1. data=http://anyurl (when scanned, mobile users can go to any URL you specify)",foreground="yellow",background="blue").grid(row=3,column=0,sticky="w")
    ttk.Label(l,text="2. data=anytext (when scanned, mobile users can read your text message)",foreground="yellow",background="blue").grid(row=4,column=0,sticky="w")
    ttk.Label(l,text="3. data=TEL:5551231234 (when scanned, mobile users can add your TEL# to their contacts and dial number)",foreground="yellow",background="blue").grid(row=5,column=0,sticky="w")
    ttk.Label(l,text="4. data=MAILTO:me@qrickit.com (when scanned, mobile users can add your EMAIL address to their contacts and send email)",foreground="yellow",background="blue").grid(row=6,column=0,sticky="w")
    ttk.Label(l,text="5. data=SMSTO:5551231234:anytext (when scanned, mobile users can add your SMS# to their contacts and send SMS message)",foreground="yellow",background="blue").grid(row=7,column=0,sticky="w")
    ttk.Label(l,text="6. data=<?php echo urlencode($yourdata);?> (example using PHP to specify \"data\")",foreground="yellow",background="blue").grid(row=8,column=0,sticky="w")
    for child in l.winfo_children():
        child.grid_configure(pady=10)

def about():
    global r4
    r4=Toplevel(root)
    r4.title("About this")
    r4.resizable(False,False)
    r4.iconbitmap("icon.ico")
    mf4=ttk.Frame(r4,padding='3 3 12 12')
    mf4.pack(fill="both",expand="yes")
    mf4.rowconfigure(0,weight=1)
    mf4.columnconfigure(0,weight=1)
    l=ttk.Label(mf4,background="blue")
    l.pack(fill="both",expand="yes")
    ttk.Label(l,text="Created By: Hrithik Raj",foreground="yellow",background="blue",font=("Arial Black",16)).grid(row=2,column=0,columnspan=2)
    img=ImageTk.PhotoImage(Image.open("icon.ico"))
    imglbl=ttk.Label(l,background="#004080",image=img)
    imglbl.photo=img
    imglbl.grid(row=4,column=0,rowspan=3)
    ttk.Label(l,text="QR Code Generator",foreground="yellow",background="blue",font=("Calibri",16)).grid(row=4,column=1)
    ttk.Label(l,text="Version : v1.0.0",foreground="yellow",background="blue",font=("Calibri",16)).grid(row=5,column=1)
    ttk.Separator(l,orient="horizontal").grid(row=6,column=0,columnspan=3,sticky="ew")
    ttk.Label(l,text="Email : hrithikraj137@gmail.com",foreground="yellow",background="blue",font=("Calibri",14)).grid(row=7,column=1)
    glbl=ttk.Label(l,text="Github : https://github.com/Cyborg117",foreground="yellow",background="blue",font=("Calibri",14),cursor="hand1")
    glbl.grid(row=9,column=1)
    glbl.bind('<1>',lambda e: webbrowser.open("https://github.com/Cyborg117"))
    for child in l.winfo_children():
        child.grid_configure(pady=10)

def qtextcolorset():
    temp=colorchooser.askcolor()[1]
    if(temp==None):
        qtextcolor.set("None")
    else:
        qtextcolor.set(temp.replace('#',''))

def fcolorset():
    temp=colorchooser.askcolor()[1]
    if(temp==None):
        fcolor.set("None")
    else:
        fcolor.set(temp.replace('#',''))

def bcolorset():
    temp=colorchooser.askcolor()[1]
    if(temp==None):
        bcolor.set("None")
    else:
        bcolor.set(temp.replace('#',''))

def generate():
    url="https://qrickit.com/api/qr.php"
    if(data.get()==""):
        msg.showerror("Status","Enter Data!!")
    else:    
        params={
            'd':data.get(),
            'addtext':qtext.get(),
            'txtcolor':qtextcolor.get(),
            'fgdcolor':fcolor.get(),
            'bgdcolor':bcolor.get(),
            't':type.get()}
        try:
            response=requests.get(url,params=params)
        except:
            msg.showerror("Status","Check Your Connection!!")
        else:
            file=open("qrcode.jpg","wb")
            file.write(response.content)
            file.close()   
            img=ImageTk.PhotoImage(Image.open('qrcode.jpg'))
            qrimg=ttk.Label(l2,image=img)
            qrimg.photo=img
            qrimg.grid(row=4,column=2)         

def download():
    fpath=filedialog.asksaveasfilename(title="Save as",filetypes=(("jpg file","*.jpg"),))
    if(fpath==""):
        fpath=os.getcwd()+"\\qr.jpg"
    else: 
        pass  
    try:
        file=open("qrcode.jpg","rb")
        imgdata=file.read()
        file.close()
    except:
        msg.showerror("Status","Generate The QR First!!")
    else:
        file=open(fpath,"wb")
        file.write(imgdata)
        file.close()

root=Tk()
root.title("Custom QR generator | By Hrithik Raj")
root.resizable(False,False)
root.iconbitmap("icon.ico")

data=StringVar()
qtext=StringVar()
qtextcolor=StringVar()
fcolor=StringVar()
bcolor=StringVar()
type=StringVar()
data_type=StringVar()

type.set('jpeg')

mainframe=ttk.Frame(root,padding='3 3 12 12')
mainframe.grid(row=0,column=0)
mainframe.rowconfigure(0,weight=1)
mainframe.columnconfigure(0,weight=1)
mf2=ttk.Frame(root,padding='3 3 12 12')
mf2.grid(row=0,column=1)
mf2.rowconfigure(0,weight=1)
mf2.columnconfigure(0,weight=1)

l=ttk.Label(mainframe,background="white")
l.pack(fill='both',expand='yes')
l2=ttk.Label(mf2,background="white")
l2.pack(fill='both',expand='yes')

ttk.Label(l,text="Custom QR Generator").grid(row=1,column=2,columnspan=5)
ttk.Label(l2,text="QR Code").grid(row=1,column=2,columnspan=5)
ttk.Label(l,text="Enter Data: ").grid(row=2,column=2)
ttk.Entry(l,textvariable=data).grid(row=2,column=3)
ttk.Button(l,text="?",command=datahelp,width=5).grid(row=2,column=4)
ttk.Label(l,text="Enter Text: ").grid(row=4,column=2)
ttk.Entry(l,textvariable=qtext).grid(row=4,column=3)
ttk.Label(l,text="Text Color: ").grid(row=6,column=2)
ttk.Entry(l,textvariable=qtextcolor).grid(row=6,column=3)
ttk.Button(l,text="select",command=qtextcolorset).grid(row=6,column=4)
ttk.Label(l,text="Foreground Color: ").grid(row=8,column=2)
ttk.Entry(l,textvariable=fcolor).grid(row=8,column=3)
ttk.Button(l,text="select",command=fcolorset).grid(row=8,column=4)
ttk.Label(l,text="Background Color: ").grid(row=10,column=2)
ttk.Entry(l,textvariable=bcolor).grid(row=10,column=3)
ttk.Button(l,text="select",command=bcolorset).grid(row=10,column=4)
ttk.Label(l,text="Image Type: ").grid(row=12,column=2)
imgtype=ttk.Combobox(l,textvariable=type)
imgtype['values']=['jpeg','png','svg']
imgtype.configure(state='readonly')
imgtype.grid(row=12,column=3)
ttk.Button(l,text="Generate",command=generate).grid(row=14,column=2)
ttk.Button(l,text="Download",command=download).grid(row=14,column=3)
ttk.Button(l,text="About",command=about).grid(row=14,column=4)

for child in l.winfo_children():
    child.grid_configure(padx=10,pady=10)

root.mainloop()
   
