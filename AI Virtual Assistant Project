# Python-Projects
# AI Voice Assistance Python Code

import time
from ipaddress import ip_address
import random
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType


import pyautogui
import pywhatkit as kit
import cv2
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyjokes
import os
import smtplib
import sys

import wolframalpha as wolframalpha
from requests import get

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak('Please wait system initializing loading disks security checkups launching user interface...system initialized')
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    elif hour >= 18 and hour <= 19:
        speak("Good Evening!")

    else:
        speak("Good Night!")

    speak("Hi, I am FRIDAY, also known as Female Replacement Intelligent Digital Assistant Youth is a natural-language user interface created by Mohammed Faiz ")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source, timeout=5, phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said:  {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return query



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("faizishaikh0809@gmail.com", "Shaikh#0809")
    server.sendmail("faizishaikh0809@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)

        elif 'hi friday' in query:
            speak('Hi Boss, how r u doing')

        elif 'good' in query:
            speak('happy to hear that boss')
            cu = takeCommand().lower()
            speak('im also good')

        elif 'tell about yourself' in query:
            speak('I am Friday , An Artificial Intelligence Program develped by Mfs')

        elif 'are you here' in query:
            speak('yes i am here only, just was thinking about some other AIs')
            ck = takeCommand().lower()
            speak('i was thinking about alexa and siri, day by day they are increasing there users')
            ci = takeCommand().lower()
            speak('Thank u boss!')
            ce = takeCommand().lower()
            speak('now im blushing boss...please stop')

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('boss, what should i search on google')
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\MD WASIM SHAIKH\\Music\\DR'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"boss, The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\MD WASIM SHAIKH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)



        elif 'open python' in query:
            pypath = "C:\\Users\\MD WASIM SHAIKH\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\idlelib\\idle.pyw"
            os.startfile(pypath)

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(1)

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")
            print(ip)

        elif 'play songs on youtube' in query:
            kit.playonyt("see you again")



        elif 'email to sam' in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to = "faizshaikh0809@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my Friend harry bhai.. i am not able to send it")


        elif 'you can sleep' in query:
            speak('thanks for using me boss, have a nice day, we will meet soon')
            sys.exit()

       

        elif 'set alarm' in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 22:
                music_dir = 'C:\\Users\\MD WASIM SHAIKH\\Music\\DR'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))


        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)


        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.time.sleep(1)
            pyautogui.keyUp("alt")

        speak("boss, do you have any other work")
