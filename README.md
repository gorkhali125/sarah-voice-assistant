# Introduction

Sarah is your assistant. She can recognize your voice and perform certain operations based on your input. Sarah is primarily targeted for Ubuntu users and is written in Python3. Sarah uses Google Text to Speech (gTTS) library for voice output.


# Requirements

1. Python3
2. SpeechRecognition
3. gTTS
4. pyjokes
5. wikipedia

# Installation

## Speech Recognition

Install SpeechRecognition using pip3. Please have a look at https://pypi.org/project/SpeechRecognition/ for more instructions. Make sure that all it's dependencies are fulfilled before installing.
```
sudo apt-get install python3-pyaudio

pip3 install SpeechRecognition
```

## gTTS

Install gTTS using pip3.
```
pip3 install gTTS
```

## pyjokes

Install pyjokes using pip3.
```
pip3 install pyjokes
```

## wikipedia

Install wikipedia using pip3.
```
pip3 install wikipedia
```

# Running Sarah

On the root directory, use the following command on a terminal window to run Sarah:
```
python3 sarah.py
```
Sarah can only take your commands when you have asked her to actually start the recognition process. To do so, command her **Start Listening** and she will do so. A list of commands are provided in the "Voice Commands" section below.

# Voice Commands

Voice commands are listed in the "queries.json" file. Please do not change anything in this json file. Here are some of the voice commands which you can use to converse with Sarah.

## Start/Stop Sarah

- Start Listening
- Stop Listening

## Text Commands

- How are you
- What is your name
- Who created you
- What is love


## System Commands

- **Powerpoint** (Open a new LibreOffice Impress)
- **Excel** (Open a new LibreOffice Calc)
- **Writer** (Open a new LibreOffice Writer)
- **Time** (Command Sarah to tell you the current time)
- **Vs code** (Open vscode if installed)
- **Tell me a joke** (Command Sarah to tell you a joke)
- **Wikipedia {searchText}** (This will search the searchText in wikipedia and read you the first sentence from wikipedia. Example: Wikipedia google)
- **Shutdown system** (Shutdown your system. Shutdown defaults to 1 minute after current time)
- **Restart system** (Restart your system. Restart defaults to 1 minute after current time)
- **Cancel shutdown** (Cancel the scheduled shutdown)
- **Cancel restart** (Cancel the scheduled restart)
  

## Browser Commands

- **Open youtube** (Opens a new youtube window)
- **Open google** (Opens a new google window)
- **Open stack overflow** (Opens a new stackoverflow window)
- **Search youtube {searchText}** (Search searchText on youtube. Example: search youtube adele hello)
- **Search google {searchText}** (Search searchText on google. Example: search google adele hello)
- **Search stackoverflow {searchText}** (Search searchText on stackoverflow. Example: search stackoverflow python get current time)
  
## Other Commands

- **Take a note** (Command Sarah to take a note. Note will be saved in your home directory with the name 'sarah-note.txt'). Each time you take a note, it will be added to the same time with the timestamp when the note was taken.
