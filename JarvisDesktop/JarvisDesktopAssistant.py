import pyttsx3 #pip install
import datetime
import speech_recognition as sr #pip install
import pyaudio #If you have error in pip install pyaudio Then try First: 'pip install pipwin' and then Second: 'pipwin install pyaudio'
import wikipedia #pip install
import webbrowser
import os
import smtplib #inbuilt


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)




def speak(audio):
    engine.say(audio) #this function will enable the voice of the system to speak
    engine.runAndWait()  # on default there are two two voices male or female but you can add more by installing packages

def wishMe():  # this function will wish the respective client by taking into account the time
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning its time to make the day productive")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon I am Harvis")

    else:
        speak("GOOD EVENING!") 

def takeCommand():
    #it takes microphine input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = .5
        audio = r.listen(source)


    try:   # so we used try and except because we don't want this code to just stop running because of a small bug
        print("Processing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print('Please say that again')
        return "None"

    return query  


def sendEmail(to,content): #this will simply send email by interpreting what you say
    server = smtplib.SMTP('smtp.gmail.com',587)  #587 is the port
    server.ehlo()
    server.starttls()
    server.login('your email','your password')
    server.sendmail('your email',to,content)
    server.close()     







if __name__ == "__main__":
    #speak("SUPRATIM IS GREAT")
    wishMe()

    while True:
        query=takeCommand().lower()
    #logic for executing task on query
    
        if 'wikipedia' in query: #for searching in wikipedia
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentence = 2)
            speak("According to Harvis")
            print(results)
            speak(results)

        elif 'open youtube' in query: #for opening youtube
            webbrowser.open("youtube.com")

        elif 'open google' in query: #for opening google
            webbrowser.open("google.com")

        elif 'open quick learn' in query: #for opening quiklrn
            webbrowser.open("quiklrn.com")

        #elif 'play music' in query:    #code for playing music
        #mus_dir = 
        #songs = os.listdir(mus_dir)
        #print(songs)
        #os.startfile(os.path.join(mus_dir, songs[0]))

        elif 'the time' in query: #will tell the time
            str = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {str}")

        elif 'who created' in query:  #creator's info
            speak(f"I was created by Mister Supratim Majumder Who was bored and made me.")


        elif 'open code' in query:  #opening visual studio code
            codepath = "C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'send email' in query:  #will send email just have to give your email and password which is not recommended
            try:
                speak('What to say?')
                content = takeCommand()
                to = "your email"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry bhai. I am not able to send this email")