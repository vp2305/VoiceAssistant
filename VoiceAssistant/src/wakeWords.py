'''
Created on 2020 M12 14

@author: Vaibhav Patel
'''
def wakeWords(command):
    WAKE_WORDS = ['hey jarvis', 'hello jarvis', 'okay jarvis']
    text = command.lower()
    
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
    
    return False