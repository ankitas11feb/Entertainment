import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import webbrowser
import pyautogui
from PyDictionary import PyDictionary
import wikipedia
from datetime import date, time
import mysql.connector
from mysql.connector import Error
from pyttsx3 import engine


def engine_speak(ask):
    pass


class User():
    print()
    print()
    print('Loading your AI personal assistant - Flixy ...')
    print("Please wait...")
    print()
    print()

    listener = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 150)
    engine.setProperty('voice', voices[0].id)
    wake = "shane"

    def speak(text):
        engine.say(text)
        engine.runAndWait()

    def engine_speak(text):
        text = str(text)
        engine.say(text)
        engine.runAndWait()

    def record_audio(ask=""):
        with sr.Microphone() as source:  # microphone as source
            if ask:
                engine_speak(ask)
            voice = listener.listen(source, 5, 5)  # listen for the audio via source
            print("Done Listening")

    count = 0
    multi_answer = 5

    # wake up
    def sayCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            pyttsx3.speak("Please say something")
            r.pause_threshold = 1
            audio = r.listen(source)
            print("Recognizing...")
            asd = r.recognize_google(audio, language='en-in', show_all=True)
            print(asd)
            pyttsx3.speak("I am ready")
            print("How may i help you...")

    def take_command(self):
        try:
            with sr.Microphone() as source:
                print('listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'flixy' in command:
                    command = command.replace('flixy', '')
                    print(command)

        except:
            pass
        return command

    def run_flixy(self):
        command = take_command(self)
        print(command)

        if 'play song' in command:
            #    save(self, command)
            song = command.replace('play', '')
            a = 'playing ' + song
            ans(a)
            print(a)
            speak(a)
            pywhatkit.playonyt(song)


        elif 'help me sleep' in command:
            #    save(self, command)
            search_term = command.split("for")[-1]
            url = f"https://www.youtube.com/watch?v=UONvpzG7yjo"
            webbrowser.get().open(url)
            a = 'Here is what I found for ' + search_term
            ans(a)
            print(a)
            speak(f'Here is what I found for {search_term} ')

        elif 'play relaxing music' in command:
            #    save(self, command)
            search_term = command.split("for")[-1]
            url = f"https://www.youtube.com/watch?v=2OEL4P1Rz04"
            webbrowser.get().open(url)
            a = 'Here is what I found for ' + search_term
            ans(a)
            print(a)
            speak(f'Here is what I found for {search_term} ')

        else:
            #    notsave(self, command)
            a = "i dont know, Please say the command again"
            ans(a)
            print(a)
            speak(a)

    sayCommand()
    while True:
        run_flixy(self)


u = User()
