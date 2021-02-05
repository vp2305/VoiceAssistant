'''
Created on 2020 M12 17

@author: vaibh
'''
def openApp(n_command):
    application_dec = {
        "onenote" : "C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE",
        "steam": "C:\\Program Files (x86)\\Steam\\steam.exe",
        "word" : "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
        "sublime text" : "C:\\Program Files\\Sublime Text 3\\sublime_text.exe",
    }
    return application_dec[n_command]