import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests

# sapi5 ist eine von microsoft Text-to-Speech Engine
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# 1 ist weibliche Stimme und 0 ist eine männliche Stimme
engine.setProperty('voice','voices[0].id')

# Die Engine wird weiter initialisiert
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Die KI soll einen Grüßen, je nach aktueller Tageszeit
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Guten Morgen")
        print("Good Morning")
    elif hour>=12 and hour<18:
        speak("Mittag")
        print("Good Afternoon")
    else:
        speak("Guten Abend")
        print("Good Evening")


#  Einrichtung der wichtigsten Befehlsfuktionen
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='de-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Ich hab dich leider nicht verstanden, bitte wiederhole dein Gesprochenes")
            return "None"
        return statement

print("Loading your AI personal assistant Kai")
#speak("Lade deine persönlichen AI Kai")
wishMe()

# Beginn der Eingabe von dem Nutzer
if __name__=='__main__':

    while True:
        speak("Wie kann ích dir helfen?")
        # Das gesprochene wird in Statement gespeichert
        statement = takeCommand().lower()
        if statement==0:
            continue

# Beenden der Voice Assistent
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('Ich schalte mich jetzt aus. Tschüss')
            print('your personal assistant Kai is shutting down,Good bye')
            break

# Suche in Wikipedia nach etwas bestimmten
        if 'wikipedia' in statement:
            speak('Suche in Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("Laut Wikipedia")
            print(results)
            speak(results)

# Öffnet YouTube
        elif 'öffne youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Youtube ist geöffnet")
            time.sleep(5)

# Gibt die aktuelle Zeit aus
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Es ist {strTime}")

# Öffnet die Top Storie Seite von Google News auf
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://news.google.com/topstories")
            speak('Hier sind ein paar Schlagzeilen. Viel Spaß beim lesen!')
            time.sleep(6)

# Sucht etwas in Google und öffnet es im Browser
        elif 'Suche'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

# Wer bist du / Was kannst du
        elif 'Wer bist du' in statement or 'Was kannst du' in statement:
            speak('Ich bin Kai dein persönlicher Assistent. Ich wurde programmiert um dich zu unterstützen'
                  'Ich kann in Wikipedia suchen, aktuelle News von Google anzeigen und noch viel mehr. Probier mich doch einfach mal aus' 
                  'Ich bin überall. Aber meistens bin ich auf Domenic`s PC. Ich kann vieles, was er mir beigebracht hat.')

# Wer hat dich gemacht
        elif "Wer hat dich gemacht" in statement or "Wer hat dich erstellt" in statement:
            speak("Ich wurde von Domenic erstellt")
            print("Mein Schöpfer Domenic hat mich geschaffen")