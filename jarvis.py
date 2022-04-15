import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random

from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import sys





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[2].id)
engine.setProperty('voices',voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=20)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis . pleae tell me how can i help you")



if __name__ == "__main__":
    takecommand()
    speak("hello jarvis")
    wish()
   # while True:
    if 1:

        query = takecommand().lower()

        #logic building for tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif "open Google Chrome" in query:
            apath = "C:\\Users\\Public\\Desktop\\Google Chrome.lnk"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open youtube" in query:
            bpath = "C:\\Users\\ma196\\Desktop\\YouTube.lnk"
            os.startfile(bpath)

        elif " open Movies" in query:
            cpath = "C:\\Users\\ma196\\Documents\\Movies"
            os.startfile(cpath)

        elif " open camera " in query:
            dpath ="C:\\Users\\ma196\\Recent\\ms-contact-support--windows-camera-app-0xA00F4244SearchKey=Windows%20Camera%20App%20error%20code%200xA00F4244.lnk"
            os.startfile(dpath)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitkey(50)
                if k==27:
                    break;
                cap.release()
                cv2.destroyWindow()

        elif "play music" in query:
            music_dir ="C:\\Users\\ma196\\Music\\Video Projects"
            songs = os.listdir(music_dir)
            rd =  random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "ip address" in  query:
            ip = get('http://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif"wikipedia" in query:
            speak("Searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)

        elif "open Instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open github" in query:
            webbrowser.open("www.github.com")

        elif "open google" in query:
            speak("what should i search in google")
            webbrowser.open("www.google.com")

        elif "send message" in query:
            kit.sendwhatmsg("+919943833945","hi how are you",2,12)

        elif " play songs on youtube" in query:
            kit.playonyt("faded")

        elif "no thanks" in query:
            speak("thanks for using me, have a good day")
            sys.exit()

            speak("do you have any other work")






