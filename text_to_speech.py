import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
from PIL import Image, ImageTk


root =Tk()
root.title("Text to Speech")
root.geometry("900x450+200+300")
root.resizable(False,False)
root.configure(bg='#034f84')
# root.configure(bg='#305065')

engine=pyttsx3.init()

def speaknow():
    text=text_area.get(1.0,END)
    
    if text == "Type here":
        return  # Prevent speaking if only the placeholder text is there


    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices = engine.getProperty("voices")
    
    
    def setvoice():
        if gender == "Female":
            engine.setProperty("voice", voices[1].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty("voice", voices[0].id)
            engine.say(text)
            engine.runAndWait()
            
    if text:
        if speed == "Fast":
            engine.setProperty("rate", 250)
            setvoice()
        elif speed == "Normal":
            engine.setProperty("rate", 150)
            setvoice()
        else:
            engine.setProperty("rate", 60)
            setvoice()
        
    

def download():
    text=text_area.get(1.0,END)
    
    # Check if the text area is empty or contains only the placeholder
    if text == "Type here" or not text:
        show_notification("Please type something first before saving")
        return  # Prevent saving if only the placeholder text is present
    
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices = engine.getProperty("voices")
    
    
    def setvoice():
        if gender == "Female":
            engine.setProperty("voice", voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,"text.mp3")
            engine.runAndWait()
            show_notification(f"File saved to {path}")
        else:
            engine.setProperty("voice", voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,"text.mp3")
            engine.runAndWait()
            show_notification(f"File saved to {path}")
            
    if text:
        if speed == "Fast":
            engine.setProperty("rate", 250)
            setvoice()
        elif speed == "Normal":
            engine.setProperty("rate", 150)
            setvoice()
        else:
            engine.setProperty("rate", 60)
            setvoice()
            
# Placeholder functions
def add_placeholder(event=None):
    if not text_area.get(1.0, END).strip():
        text_area.insert(1.0, "Type here")
        text_area.config(fg="grey")

def remove_placeholder(event=None):
    if text_area.get(1.0, END).strip() == "Type here":
        text_area.delete(1.0, END)
        text_area.config(fg="black")
        
def show_notification(message):
    # Create a label to show the notification
    notification_label = Label(root, text=message, font="arial 12", bg="yellow", fg="black")
    notification_label.place(x=550, y=350)  
    
    root.after(3000, notification_label.destroy)



#icon
image = Image.open("speak.png")
image_icon = ImageTk.PhotoImage(image)
root.iconphoto(False,image_icon)

#Frame
top_frame=Frame(root,bg="#92a8d1",width=900,height="100")
top_frame.place(x=0,y=0)

#Logo
logo = Image.open("speaker logo.png")
logo_icon = ImageTk.PhotoImage(logo)  # Convert to ImageTk.PhotoImage
Label(top_frame, image=logo_icon, bg="#92a8d1").place(x=10, y=5)  # Use logo_icon here

Label(top_frame,text="Text to Speech",font="arial 20 bold",bg="#92a8d1",fg='black').place(x=100,y=30)


text_area=Text(root,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)
text_area.insert(1.0, "Type here")
text_area.config(fg="grey")

# Bind focus in/out events for placeholder
text_area.bind("<FocusIn>", remove_placeholder)
text_area.bind("<FocusOut>", add_placeholder)

Label(root,text="VOICE",font="arial 15 bold",bg='#305065',fg="white").place(x=570,y=160)
Label(root,text="SPEED",font="arial 15 bold",bg='#305065',fg="white").place(x=750,y=160)

gender_combobox=Combobox(root,values=['Female','Male'],font="arial 14",state='r',width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set("Female")

speed_combobox=Combobox(root,values=['Fast','Normal','Slow'],font="arial 14",state='r',width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set("Normal")

speakicon=PhotoImage(file="speak.png")
btn=Button(root,text="Speak",compound=LEFT,image=speakicon,width=130,font="arial 14 bold",command=speaknow)
btn.place(x=550,y=280)


downloadicon=PhotoImage(file="download.png")
btn=Button(root,text="Save",compound=LEFT,image=downloadicon,width=130,bg='#39c790',font="arial 14 bold",command=download)
btn.place(x=730,y=280)


# Confirmation message label
confirmation_label = Label(root, text="", font="arial 12", bg='#305065', fg="white")
confirmation_label.place(x=550, y=350)


# Trigger placeholder on startup
add_placeholder()

root.mainloop()