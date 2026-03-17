import os
import speech_recognition as sr
import pyttsx3
import ollama
import webbrowser
import pyautogui
import pywhatkit
import wikipedia

# Voice engine
engine = pyttsx3.init()
engine.setProperty("rate",170)

def clear_terminal():
    os.system("cls")

def speak(text):
    print("Jini:", text)
    engine.say(text)
    engine.runAndWait()

def listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except:
            return ""

    try:
        command = r.recognize_google(audio)
        command = command.lower()
        print("You:", command)
        return command

    except:
        return ""

def ai_answer(question):

    try:
        response = ollama.chat(
            model="llama3:latest",
            messages=[
                {"role":"system","content":"You are Jini AI assistant. Give short answers."},
                {"role":"user","content":question}
            ]
        )

        return response["message"]["content"]

    except:
        return "Sorry Prashik, AI is not available right now."


speak("Hello Prashik. Say Hey Jini to activate.")

active = False

clear_terminal()

while True:

    command = listen()

    if command == "":
        continue

    # END PROGRAM
    if "end program" in command or "shutdown jini" in command:
        speak("Goodbye Prashik")
        clear_terminal()
        break


    # WAKE UP
    if not active and ("jini" in command or "genie" in command or "jenny" in command):
        active = True
        speak("I am ready. What do you need?")
        continue


    if active:

        # YOUTUBE
        if "youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        # GOOGLE
        elif "google" in command:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        # SEARCH
        elif "search" in command:
            query = command.replace("search","")
            speak("Searching")
            pywhatkit.search(query)

        # PLAY SONG
        elif "play" in command:
            song = command.replace("play","")
            speak("Playing song")
            pywhatkit.playonyt(song)

        # SCROLL
        elif "scroll down" in command:
            pyautogui.scroll(-500)

        elif "scroll up" in command:
            pyautogui.scroll(500)

        # VIDEO CONTROL
        elif "pause" in command or "stop" in command:
            pyautogui.press("k")

        elif "next video" in command:
            pyautogui.press("shift+n")

        elif "previous video" in command:
            pyautogui.press("shift+p")

        # BACK PAGE
        elif "back page" in command:
            pyautogui.hotkey("alt","left")

        # WIKIPEDIA
        elif "who is" in command:
            person = command.replace("who is","")

            try:
                info = wikipedia.summary(person,2)
                speak(info)
            except:
                speak("Sorry I couldn't find information.")


        # LINKEDIN
        elif "linkedin" in command:
            speak("Opening your LinkedIn profile")
            webbrowser.open("https://linkedin.com/in/prashik-bhagat-a1973239a/")


        # WHATSAPP
        elif "whatsapp" in command:
            speak("Opening WhatsApp")
            webbrowser.open("https://web.whatsapp.com/")


        # DATA ANALYST
        elif "data analyst" in command:
            speak("Opening Data Analyst tutorial")
            webbrowser.open("https://youtu.be/8411fEhNKNc")


        # FIGMA
        elif "figma" in command:
            speak("Opening Figma tutorial")
            webbrowser.open("https://youtu.be/xgk5N4rCJIw")


        # PYTHON
        elif "python" in command:
            speak("Opening Python tutorial")
            webbrowser.open("https://youtu.be/XV-lIaO00H8")


        # NASA
        elif "nasa" in command:
            speak("Opening NASA website")
            webbrowser.open("https://www.nasa.gov/")


        # CURSOR RIGHT
        elif "cursor right" in command:
            pyautogui.moveRel(100,0)

        # CURSOR LEFT
        elif "cursor left" in command:
            pyautogui.moveRel(-100,0)

        # CURSOR UP
        elif "cursor up" in command:
            pyautogui.moveRel(0,-100)

        # CURSOR DOWN
        elif "cursor down" in command:
            pyautogui.moveRel(0,100)

        # CLICK
        elif "click" in command:
            pyautogui.click()

        # NEW TAB
        elif "open new tab" in command:
            speak("Opening new tab")
            pyautogui.hotkey("ctrl","t")

        # CLOSE TAB
        elif "close tab" in command:
            speak("Closing tab")
            pyautogui.hotkey("ctrl","w")

        # NEXT TAB
        elif "next tab" in command:
            pyautogui.hotkey("ctrl","tab")

        # PREVIOUS TAB
        elif "previous tab" in command:
            pyautogui.hotkey("ctrl","shift","tab")

        else:
            answer = ai_answer(command)
            speak(answer)