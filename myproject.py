# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 07:44:04 2023

@author: Lenovo
"""

import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator

import speech_recognition as sr

r=sr.Recognizer()
print(sr.Microphone.list_microphone_names())
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source,duration=1)
    # r.energy_threshold()
    print("say anything : ")
    audio= r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text)
    except:
        print("sorry, could not recognise")
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning  !")

    elif hour>= 12 and hour<18:
        speak("Good Afternoon  !")

    else:
        speak("Good Evening  !")

    assname =(" I am tech buddy, your assistant")
    speak(" I am here to help you")
    speak(assname)


def username():
    speak("What should i call you ")
    uname = takeCommand()
    speak("Welcome")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome.", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you?")
    print("how can I help you?")
def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "say again"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()
if __name__ == '__main__':
    clear = lambda: os.system('cls')


    clear()
    wishMe()
    username()

    while True:

        query = takeCommand().lower()


        if ' open wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
        elif 'open map' in query:
            speak("Here you go to map")
            webbrowser.open("https://maps.google.co.in/")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")

            webbrowser.open("spotify.com")
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            speak(f", the time is {strTime}")

        

        elif 'email to Harsheet' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Receiver email address"
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whome should i send")
                to = input()
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you")
        elif 'not good' in query or 'bad mood' in query:
             speak("That's sad to hear, I can lit your mood IF your want ")
        elif 'really' in query:
             speak("i will craking some jokes, here you go")
             webbrowser.open("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.rd.com%2Flist%2Ffunny-jokes-national-tell-joke-day%2F&psig=AOvVaw0re41AYfz8dD7p1i1toOBq&ust=1677147539817000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCMjhvtXzqP0CFQAAAAAdAAAAABAJ")

        elif ' i am fine' in query or " i am good" in query:
            speak("It's good to know that your fine")
        elif ' thankyou' in query:
            speak("it's my pleasure to help you")



        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "change name" in query:
            speak("What would you like to call me,")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif 'exit' in query or 'bye' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Charneet.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "calculate" in query:
            

            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif "why you came to world" in query:
            speak(" It's a secret")

        elif "power point presentation" in query:
            speak("opening Power Point presentation")
            power = r"C:\Users\Lenovo\Desktop\voice bot ppt.pptx"
            os.startfile(power)

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your friend")

        elif 'reason for you' in query:
            speak("I was created as a Minor project for competition ")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                    0,
                                                    "Location of wallpaper",
                                                    0)
            speak("Background changed successfully")

        elif 'open bluestack' in query:
            appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            os.startfile(appli)

        elif 'news' in query:

            

                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                webbrowser.open("https://timesofindia.indiatimes.com/news")

                


        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop tech buddy from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "tech buddy Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('hi.txt', 'w')
            

        elif "show note" in query:
            speak("Showing Notes")
            file = open("hi.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream = True)

            with open("Voice.py", "wb") as Pypdf:

                total_length = int(r.headers.get('content-length'))

                for ch in progress.bar(r.iter_content(chunk_size = 2391975),
                                    expected_size =(total_length / 1024) + 1):
                    if ch:
                                      Pypdf.write(ch)

        # NPPR9-FWDCX-D2C8J-H872K-2YT43
        elif "tech buddy" in query:

            wishMe()
            speak("Happy in your service")
            speak(assname)

        elif "weather" in query:

            
            api_key = "Api key"
            base_url = "https://worldweather.wmo.int/"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["code"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))

            else:
                speak(" City Not Found ")


        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you")
            speak(assname)



        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")
        elif "will you marry me" in query:
            speak("I am shy to Answer")
        elif "do you love me" in query:
            speak("yes, I love you so much")
        elif "how are you" in query:
            speak("I'm fine, glad you asked me that")
        elif "show some images" in query:
            speak("here, click this link to open images")
            webbrowser.open("https://www.google.com/search?q=nature+images&sxsrf=AJOqlzXpIep72GkgJ6dmm0cvCqvgUKH26A%3A1677053514251&source=hp&ei=Ss71Y8rVDLea4-EPrPOr8AY&iflsig=AK50M_UAAAAAY_XcWhaNdg2DTuARuyG-Z_zEEdKmV6B_&ved=0ahUKEwjKou-X16j9AhU3zTgGHaz5Cm4Q4dUDCAg&uact=5&oq=nature+images&gs_lcp=Cgdnd3Mtd2l6EAMyCAgAEIAEELEDMgsIABCABBCxAxCDATIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgsIABCABBCxAxCDATIFCAAQgAQyBQgAEIAEOgcIIxDqAhAnOgQIIxAnOgUIABCRAjoICAAQsQMQgwE6CwgAELEDEIMBEJECOggIABCxAxCRAlDMD1iKHmCJH2gBcAB4AIABtQKIAaYUkgEHMC42LjUuMZgBAKABAbABCg&sclient=gws-wiz")
        elif "i love you" in query:
            speak("It's hard to understand")
        elif "open food ordering sites" in query:
            speak("here you go")
            webbrowser.open("https://www.swiggy.com/")
        elif "open shopping sites" in query:
            speak("here you go")
            webbrowser.open("https://www.myntra.com/")

        elif "what is" in query or "who is" in query:


            client = wolframalpha.Client("API_ID")
            res = client.query(query)

            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")

