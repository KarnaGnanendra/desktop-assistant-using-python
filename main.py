import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening......')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command=command.lower()
            if 'captian' in command:
                command=command.replace('captian', '')
                print(command)

    except:
        pass
    return command
def run_captian():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif'time' in command:
        time=datetime.datetime.now().strftime('%I:%M:%S %p')
        print(time)
        talk('current time is ' + time)
    elif 'tell me about' in command:
        person =command.replace('tell me about','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('please say the command again')
while True:
    run_captian()