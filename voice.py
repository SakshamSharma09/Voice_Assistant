import pyttsx3
import datetime
import pyaudio
import os
import random
import pyjokes
import psutil
import wikipedia
import pyautogui
import smtplib
import webbrowser as wb
import speech_recognition as sr

engine = pyttsx3.init()
voice=engine.getProperty('voices')
speakrate = 200
engine.setProperty('voice',voice[1].id)
engine.setProperty('rate',speakrate)

def joke():
    speak(pyjokes.get_joke())
def greet():
    speak("Welcome back Sir!")
    hour = datetime.datetime.now().hour
    if (hour >= 5 and hour < 11):
        speak('Good Morning ')
    elif (hour >= 11 and hour < 16):
        speak('Good Afternoon ')
    elif (hour >= 16 and hour < 22):
        speak('Good evening ')
    else:
        speak('Good night ')

    speak("How can i help you ")

def time():
    Time=datetime.datetime.now().strftime('Current Time is %H:%M:%S')
    speak(Time)


def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    day=int(datetime.datetime.now().day)
    speak('Current date is')
    speak(day)
    speak(month)
    speak(year)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("listening....")
        r.pause_threshold  = 0.5
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio)
        print(query)

    except Exception as e:
        print(e)
        speak("plz speak that again")

        return "None"

    return query

def sendmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("test@gmail.com","test123")
    server.sendmail("test@gmail.com",to,content)
    server.close()

def screenhot():
    img = pyautogui.screenshot()
    img.save("C:/Users/Saksham/OneDrive/Desktop/VoiceAssistantScreenShots/ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at "+ usage)
    battery=psutil.sensors_battery()
    speak("Battery Prcentage is: ")
    speak(battery.percent)


if __name__ == '__main__':

    greet()

    while True:
        query = command().lower()
        print(query)

        if "how are you" in query:
            speak("I'm fine sir, how can i help you ?")
        elif "who are you" in query:
            speak("Sir I am your personal assistant ")
        elif "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            speak("Ok sir!")
            quit()
        elif "day" in query:
            day=datetime.datetime.now().weekday()
            speak(day)
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=3)
            speak("wikipedia says")
            print(result)
            speak(result)
        elif "send email" in query:
            try:
                speak("what content is to be sent")
                content = command()
                to = "xyz@gmail.com"
                sendmail(to,content)

                speak("Email has been sent successfully to "+ to)
            except Exception as e:
                print(e)
                speak("Unable to send the message")

        elif "search on internet" in query:
            speak("What should I search")
            search = command().lower()
            wb.open_new_tab(search + ".com")

        elif "log out" in query:
            os.system("shutdown - l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "play audio song" in query:
            songs_dir = "E:\MUSIC"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
        elif "play video song" in query:
            vsongs_dir = "E:\Videos\MusicVideos"
            vsongs = os.listdir(vsongs_dir)
            os.startfile(os.path.join(vsongs_dir,vsongs[0]))

        elif "remember that" in query:
            speak("what to remember")
            data = command()
            speak("you asked me to remember that " + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        elif "did you remember" in query:
            remember = open("data.txt","r")
            speak("you said me to remember that " + remember.read())
        elif "screenshot" in query:
            screenhot()
            speak("Done")
        elif "cpu" in query:
            cpu()
        elif "joke" in query:
            joke()



