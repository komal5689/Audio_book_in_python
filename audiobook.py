#first install and then import given modules:

import os

from tkinter import *

from tkinter import Tk

from tkinter import filedialog

from gtts import gTTS

import PyPDF2

from PIL import Image ,ImageTk

def open_pdffile():

    filepath=filedialog.askopenfilename()
    pdf=PyPDF2.PdfReader(filepath)
    mytext=" "

    for pageNum in range(len(pdf.pages)):
        pageObj=pdf.pages[0]
        mytext += pageObj.extract_text()
        
        
    print(mytext)

    final_output=gTTS(text=mytext,lang='en')

    print("Generating Speech.............")

    final_output.save("Generated_Speech.mp3")

    os.system("Start Generated_Speech.mp3")

    print("Successfully Generated!")


root=Tk()


root.geometry("550x250")
root.minsize(550,250)
root.maxsize(550,250)
root.title("AUDIOBOOK")


image=Image.open("audiobook2.jpg")
photo=ImageTk.PhotoImage(image)
yash_label=Label(image=photo)
yash_label.pack()

label1=Label(root,text="Select pdf file to Convert",font=("Arial",20,"bold"),fg='white',bg='black',bd=4,relief=RIDGE)
label1.pack(padx=20,pady=20)
label1.place(x=125,y=15)


button1=Button(root,text="Select",font=("Harlow Solid",12),command=open_pdffile,width=10,height=1,bd=2,relief=RIDGE,bg='black',fg='white')
button1.pack()
button1.place(x=230,y=200)


format=StringVar()


root.mainloop()