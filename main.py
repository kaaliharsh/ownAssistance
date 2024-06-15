import webbrowser
import speech_recognition as sr
import os
import openai

def say(text):
    os.system(f"say {text}")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            print("Recognizing...")
            query=r.recognize_google(audio,language='en-in')
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error happened"



if __name__ == '__main__':
    print('PyCharm')
    say("I am your personal assistant. How can I help you?")
    while True:
        print("Listening......")
        query=takeCommand()
        sites=[["youtube","https://www.youtube.com"],["google","https://www.google.com"],["wikipedia","https://www.wikipedia.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])
       # say(query)
