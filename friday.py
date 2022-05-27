import pyttsx3
friend = pyttsx3.init()
speech = input("say somethng:")
friend.say(speech)
friend.runAndWait()
