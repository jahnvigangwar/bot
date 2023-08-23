import speech_recognition as sr
import os
## import subprocess, sys
import webbrowser
import datetime

def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Rcogonizing    ")
            query = r.recognize_google(audio, language = "en-in") # "hi-in"
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error occured! sorry"



if __name__ == '__main__':
    print('PyCharm')
    say("Hello I am Jahnveess bot")
    while True:
        print("Listening  ...")
        text = takeCommand()
        sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"], ["google", "https://google.com"]]
        # say(text)
        for site in sites:
            if f"Open {site[0]}".lower() in text.lower():
                webbrowser.open(site[1])
                say("Opening {site[0]} yayyyy")

        if f"open music" in text.lower():
            musicPath = "/Users/apple/Downloads/vinee-heights-126947.mp3"
            # os.startfile(musicPath)
            ## opener = "open" if sys.platform == "darwin" else "xdg-open"
            ## subprocess.call([opener, musicPath])
            os.system(f"open {musicPath}")

        if f"the time" in text.lower():
            strfTime = datetime.datetime.now().strftime("%H : %M: %S")
            say(f"The time is {strfTime}")


