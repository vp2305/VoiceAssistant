'''
Created on 2020 M12 14

@author: Vaibhav Patel
'''
import random
def greeting(command):
    
    GREETING_INPUTS = ["hi", "hey", "hello"]
    
    GREETING_RESPONSES = ["hello, how can I help you today?", 
                          "hey there, what do you want me to do?",
                          "howdy, what do you want me to do?"]
    
    for word in command.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + "."    
    return ''
