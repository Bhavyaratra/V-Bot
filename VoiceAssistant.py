from tkinter import *
import os
import pyttsx3 
import speech_recognition as sr
import random
import webbrowser
import datetime
import wikipedia 
import time

window = Tk()
window.geometry("300x500")


engine = pyttsx3.init('sapi5')
engine.setProperty("rate",140)


def read_text(audio):
    engine.say(audio)
    engine.runAndWait()

def voice_cmd():
    r=sr.Recognizer()    
    with sr.Microphone() as source:
        print("-Listening-")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("-Recognizing-")    
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return query

def start():
    read_text("How may i help you ")    
    print("How may i help you ") 

    while True:
        query = voice_cmd().lower() 

        if 'weather' in query:
            print("ok")
            os.system("Python weather_app.py")

        elif 'tic tac toe' in query:
            os.system("Python tictactoe.py")  

        elif 'roll dice' in query:
            number = random.randint(1,6)         
            print(number)

        elif 'open youtube' in query:
            read_text("Opening Youtube")
            print("Opening Youtube")
            webbrowser.get('windows-default').open("youtube.com") 

        elif 'open google' in query:
            read_text("Opening Google")
            webbrowser.open("google.com")  

        elif 'wikipedia' in query:
            read_text('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            read_text("According to Wikipedia")
            print(results)
            read_text(results)         

window.title("Assistant")

img= PhotoImage(file = "bck.png")


label1=Label(window,image= img)
label1.place(x=0,y=0)

lf=Frame(window)
lf.pack(side=BOTTOM)



btn1 = Button(text = 'EXIT',width=25,command=window.destroy, bg = '#2ECC71')
btn1.config(font=("Courier", 12))
btn1.pack(side=BOTTOM,pady=10)

btn2 = Button(text = 'START',width = 25,command=start, bg = '#2ECC71')
btn2.config(font=("Courier", 12))
btn2.pack(side=BOTTOM,pady=5)


window.mainloop()