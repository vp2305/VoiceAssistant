"""
To-do
Math ability - Kinda done
Calender, timer - will work on it...
Add a way that jarvis know its afternoon or morning or time to sleep (Done)
How to ask for a whether right now in python    
Checks for notification
Connects to bluetooth 
learn about how threading work
put in some games, head and tails, rock paper and scissor (Done)
"""
import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import subprocess
import wikipedia
import datetime
import time
import random

from wakeWords import *
from greeting import *
from openApp import *
from sendMessage import *
from mathOp import *

listener = sr.Recognizer()
engine = pyttsx3.init()

voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)


voice_rate = engine.getProperty('rate')   # getting details of current speaking
engine.setProperty('rate', 220)     # setting up new voice rate


_, _, _, am_pm = h_m_s()
if(am_pm == 'PM'):
    engine.say("Allow me to introduce myself, I'm Jarvis.")
    engine.say("Good Afternoon, what can I do for you today?")
    engine.runAndWait()
else:
    engine.say("Allow me to introduce myself, I'm Jarvis.")
    engine.say("Good Morning, what can I do for you today?")
    engine.runAndWait()
print("Hello, I'm Jarvis. I'm here to help you out through your day :)")
print("Just say 'Hey Jarvis' and then your command.")


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Say something, I'm listening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except sr.UnknownValueError:
        print(
            "----------Sorry. I didn't catch that, please say the command again----------")
        command = take_command()
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
    return command


def ask_input():
    try:
        with sr.Microphone() as input_source:
            print("Say something, I'm listening...")
            listener.adjust_for_ambient_noise(input_source)
            v = listener.listen(input_source)
            input_command = listener.recognize_google(v)
    except sr.UnknownValueError:
        print(
            "----------Sorry. I didn't catch that, please say the command again----------")
        command = ask_input()
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
    return input_command


def run_j():
    if ("what's up" in command):
        talk("Just conducting some research, what can I do for you today?")

    elif ("who are you" in command):
        talk("I'm Jarvis, created by Vaibhav to help and assist in day to day task.")

    elif ("how are you feeling" in command):
        talk("I'm feeling good, but I'm here for you...")

    elif ("are you there" in command):
        talk("Yes, I'm right here. What happen?")

    elif ("rock paper" in command and "scissors" in command or "scissor" in command):
        print("-----------------")
        print("Rock, Paper and Scissor Game:")
        print("-----------------")
        talk("Okay, lets play, best of 3!")
        player_score = 0
        jarvis_score = 0
        for i in range(1, 4):
            r_p_s = ['rock', 'paper', 'scissor']
            talk("What do you want to choose? Rock, paper or scissor?")
            player_choice = ask_input()
            player_choice.lower()
            print('You chose: ' + player_choice)
            # 1 = Rock, 2 = Paper, 3 = Scissors
            jarvis_choice = random.choice(r_p_s)
            print('Jarvis chose: ' + jarvis_choice)

            if (player_choice == 'rock' and jarvis_choice == 'paper'):
                jarvis_score = jarvis_score + 1
                print("Jarvis wins this round.")
            elif (player_choice == 'paper' and jarvis_choice == 'scissor'):
                jarvis_score = jarvis_score + 1
                print("Jarvis wins this round.")
            elif (player_choice == 'scissors' and jarvis_choice == 'rock'):
                jarvis_score = jarvis_score + 1
                print("Jarvis wins this round.")
            else:
                player_score = player_score + 1
                print("Player wins this round.")

        if (player_score > jarvis_score):
            talk("Congratulations, You win the game!")
            talk("I will make sure to beat you in this game next time.")
            talk("Game is ending, please say the command again to play again.")
        else:
            talk("Sorry you lost this game, but come back to play another game.")
            talk("Come back to play another round.")
            talk("Game is ending, please say the command again to play again.")

    elif ('head' in command or 'heads' in command and 'tail' in command or 'tails' in command or 'flip' in command and 'coin' in command):
        coin = ['heads', 'tails']
        j_choice = random.choice(coin)
        talk("It is" + j_choice)

    elif ("calculations" in command or "calculation" in command):
        talk("Tell me what you want to calculate, example:")
        math_command = ask_input()
        print("You said: " + math_command)
        result = mathOperations(math_command)
        talk("The answer is " + str(result))

    elif ('information' in command or "summary" in command):
        n_command = command
        n_command = n_command.split("about ", 1)[1]
        talk('Wait a minute, let me pull up the information on' + n_command)
        result = wikipedia.summary(n_command, sentences=2)
        talk(result)

    elif ("play a song" in command or "play song" in command):
        talk("What song do you want to listen to?")
        input_command = ask_input()
        talk("Playing " + input_command)
        pywhatkit.playonyt(input_command)

    elif ("right now" in command and "time" in command):
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif ("joke" in command or "jokes" in command and "tell" in command):
        talk(pyjokes.get_joke())

    elif ("open" in command):
        n_command = command
        n_command = n_command.split("open ", 1)[1]
        app_location = openApp(n_command)
        subprocess.call(app_location)

    elif ("send a message" in command):
        send_message()

    elif ("search" in command in command):
        # create a separate file for this
        new_command = command.replace("search", "")
        pywhatkit.search(new_command)

    elif ("nevermind" in command or "stop" in command or "exit" in command or 'end' in command):
        talk("Okay, let me know if you need any assistant")
        exit()
    else:
        talk("Please say the command again.")


time.sleep(1)
while 1:
    command = take_command()
    response = ''
    print("You said: " + command)
    c = command
    l_command = len(c.split())

    if (wakeWords(command) == True and l_command <= 2):
        print("You said the wake word or phrase")
        response = response + greeting(command)
        print("The response: " + response)
        talk(response)

    else:
        run_j()
