'''
Created on 2020 M12 17

@author: vaibh
'''
import pyttsx3
import speech_recognition as sr
import datetime
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()

voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)


voice_rate = engine.getProperty('rate')   # getting details of current speaking
engine.setProperty('rate', 220)     # setting up new voice rate


def getNumber(in_command):
    sendMessage = {
        "name": "number"
    }
    c = in_command
    name = ""
    for n in c.split():
        if (n in sendMessage):
            name = n
    return sendMessage[name]


def reask_input():
    try:
        with sr.Microphone() as input_source:
            print("Listening...")
            listener.adjust_for_ambient_noise(input_source)
            v = listener.listen(input_source)
            in_command = listener.recognize_google(v)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
    return in_command


def h_m_s():
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    am_pm = datetime.datetime.now().strftime('%p')
    return hour, minute, second, am_pm


def send_message():
    engine.say("Who do you want to send?")
    engine.runAndWait()
    in_command = reask_input()
    print("You said: " + in_command)
    engine.say("What do you want to send?")
    engine.runAndWait()
    mess_text = reask_input()
    print("You said: " + mess_text)
    messenger_number = getNumber(in_command)

    hour, minute, _, _ = h_m_s()

    pywhatkit.sendwhatmsg(messenger_number, mess_text, hour, minute + 1)
