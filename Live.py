import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser
import pyautogui
import wikipedia
from datetime import date, time
import mysql.connector
from mysql.connector import Error
from pyttsx3 import engine


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
    def sayCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            speak("Please say something")
            r.pause_threshold = 1
            audio = r.listen(source)
            print("Recognizing...")
            asd = r.recognize_google(audio, language='en-in', show_all=True)
            print(asd)
            speak("I am ready")
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

    # Known Command History

    def run_flixy(self):
        command = take_command(self)
        print(command)

        # Defining live news channels & radio
        if 'latest news on aaj tak' in command:
            #    save(self, command)
            search_term = command.split("for")[-1]
            url = f"https://www.youtube.com/watch?v=GLJZ-hqa7UY"
            webbrowser.get().open(url)
            a = 'Here is what I found for ' + search_term
            ans(a)
            print(a)
            speak(f'Here is what I found for {search_term} ')

        elif 'latest news on abp news' in command:
            #    save(self, command)
            search_term = command.split("for")[-1]
            url = f"https://www.youtube.com/watch?v=DZCElJyPfG0"
            webbrowser.get().open(url)
            a = 'Here is what I found for ' + search_term
            ans(a)
            print(a)
            speak(f'Here is what I found for {search_term} ')

        elif 'latest news on india tv news' in command:
            #    save(self, command)
            search_term = command.split("for")[-1]
            url = f"https://www.youtube.com/watch?v=A6xA7Alv10c"
            webbrowser.get().open(url)
            a = 'Here is what I found for ' + search_term
            ans(a)
            print(a)
            speak(f'Here is what I found for {search_term} ')


        elif 'live radio english' in command:
            #    save(self, command)
            search_term = command.split("for")[-1]
            url = f"https://www.youtube.com/watch?v=kGKkUN50R0c"
            webbrowser.get().open(url)
            a = 'Here is what I found for ' + search_term
            ans(a)
            print(a)
            speak(f'Here is what I found for {search_term} ')

        elif 'live radio hindi' in command:
            #    save(self, command)
            search_term = command.split("for")[-1]
            url = f"https://www.youtube.com/watch?v=uBeinBM2oXI"
            webbrowser.get().open(url)
            a = 'Here is what I found for ' + search_term
            ans(a)
            print(a)
            speak(f'Here is what I found for {search_term} ')

        elif 'help me sleep' in command:
            #    save(self, command)
            search_term = command.split("for")[-1]
            url = f"https://www.youtube.com/watch?v=UONvpzG7yjo"
            webbrowser.get().open(url)
            a = 'Here is what I found for ' + search_term
            ans(a)
            print(a)
            speak(f'Here is what I found for {search_term} ')


        elif 'latest headlines' in command:
            #    save(self, command)
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            a = 'Here are some headlines from the Times of India,Happy reading'
            ans(a)
            print(a)
            speak(a)
            speak(news)

        else:
            #    notsave(self, command)
            a = "i dont know, Please say the command again"
            ans(a)
            print(a)
            speak(a)

    sayCommand()
    while True:
        run_flixy()


u = User()
