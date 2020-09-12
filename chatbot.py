import pyttsx3
import sppechrecognition
import wikipedia

import datetime
import os
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print("JARVIS: ", audio)
  
def wishMe():
   speak("hello")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You: {query}\n")
        
       
    except Exception as e:
        print(e)
        print("Sorry, Please say that again...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https:\\www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https:\\www.google.com")

        elif 'play music' in query:
            music_dir = 'E:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[3]))
            
        elif 'open code ' in query:
            codePath = 'A:\\vs code\\Microsoft vs code\\Code.exe'
            os.startfile(codePath)
        elif 'hi' in query:
            speak("Congratulation")
        elif 'hello' in query:
            speak("Congratulation")
        elif 'thanx' in query:
            speak("here is surprise for you")