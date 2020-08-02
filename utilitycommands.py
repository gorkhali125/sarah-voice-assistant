import audioprocessor as ap
import time
from os.path import expanduser


def utilityCommands(text):
    if(text == 'take a note'):
        note_text = ap.listen()
        if(note_text != ""):
            home = expanduser("~")
            file = open(home + '/' + 'sarah-note.txt', 'a')
            file.write(time.ctime())
            file.write(" :- ")
            file.write(note_text)
            file.write("\n")
            ap.say("Note saved in your home directory")
        else:
            ap.say("Could not understand note text")