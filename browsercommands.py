import audioprocessor as ap
import webbrowser


def browserCommands(text, answer):
    if(text == "open youtube"):
        webbrowser.open("http://youtube.com")

    elif(text == "open google"):
        webbrowser.open("http://google.com")

    elif(text == "open stack overflow"):
        webbrowser.open("http://stackoverflow.com")

    elif("search youtube" in text):
        query = text.replace("search youtube", "").strip()
        if(query == ""):
            ap.say("Sorry! I cannot find anything to search for...")
        else:
            answer = answer.replace("{searchText}", query)
            ap.say(answer)
            webbrowser.open("https://www.youtube.com/results?search_query=" + query)

    elif("search google" in text):
        query = text.replace("search google", "").strip()
        if(query == ""):
            ap.say("Sorry! I cannot find anything to search for...")
        else:
            answer = answer.replace("{searchText}", query)
            ap.say(answer)
            webbrowser.open("https://www.google.com/search?q=" + query)

    elif("search stackoverflow" in text):
        query = text.replace("search stackoverflow", "").strip()
        if(query == ""):
            ap.say("Sorry! I cannot find anything to search for...")
        else:
            answer = answer.replace("{searchText}", query)
            ap.say(answer)
            webbrowser.open("https://stackoverflow.com/search?q=" + query)
